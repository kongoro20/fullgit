#!/bin/bash

LOCK_FILE="/tmp/open_sh.lock"
LOG_OUT="/root/replay_out.log"
LOG_ERR="/root/replay_err.log"
MAX_RETRIES=10  # Number of retries to attempt if Firefox fails to open
RETRY_DELAY=5  # Delay between retries in seconds

if [ -f "$LOCK_FILE" ]; then
    echo "⚠️ Warning: Another instance of open.sh is already running!" | tee -a "$LOG_OUT"
    exit 1
fi
touch "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT  # Remove lock file on exit

export DISPLAY=:1
export XAUTHORITY=/root/.Xauthority
export MOZ_DISABLE_RDD_SANDBOX=1
export NO_AT_BRIDGE=1
export MOZ_GL_ALWAYS_SOFTWARE=1  # Disable hardware acceleration
export MOZ_NO_SOUND=1  # Disable sound
export MOZ_DISABLE_GMP_SANDBOX=1
export MOZ_DISABLE_A11Y=1  # Accessibility issues (optional)

echo "🚀 Starting open.sh..." | tee -a "$LOG_OUT"

# Kill any existing Firefox instances
echo "🔪 Killing any stuck Firefox processes..." | tee -a "$LOG_OUT"
pkill -f firefox
sleep 2

# Read profile
if [ ! -f current_profile.txt ] || [ ! -s current_profile.txt ]; then
    echo "❌ Error: current_profile.txt is missing or empty!" | tee -a "$LOG_ERR"
    exit 1
fi

PROFILE_NAME=$(cat current_profile.txt | tr -d '[:space:]')
PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name "*$PROFILE_NAME*" | head -n 1)

if [ -z "$PROFILE_DIR" ]; then
    echo "❌ Error: Profile '$PROFILE_NAME' not found!" | tee -a "$LOG_ERR"
    exit 1
fi

echo "✅ Found profile: $PROFILE_DIR" | tee -a "$LOG_OUT"

# Retry mechanism for opening Firefox
for attempt in $(seq 1 $MAX_RETRIES); do
    echo "🔥 Attempting to start Firefox, attempt $attempt of $MAX_RETRIES..." | tee -a "$LOG_OUT"
    firefox --no-remote --new-instance --profile "$PROFILE_DIR" --purgecaches --display=:1 > /dev/null 2>> "$LOG_ERR" &  # No new window
    sleep 3

    # Check if Firefox process is running
    if pgrep -fa "firefox.*$PROFILE_NAME" > /dev/null; then
        echo "✅ Firefox process detected!" | tee -a "$LOG_OUT"
        break
    fi

    # If Firefox failed to start, clean caches and retry
    echo "❌ Firefox did not start. Cleaning caches and retrying..." | tee -a "$LOG_ERR"
    pkill -f firefox  # Kill any existing Firefox processes
    sleep 2
    rm -rf "$PROFILE_DIR/cache2"  # Remove any cached files
    sleep $RETRY_DELAY
done

# Ensure Firefox window is visible
echo "🕒 Waiting for Firefox window..." | tee -a "$LOG_OUT"
for i in {1..15}; do
    if wmctrl -l | grep -i "Mozilla Firefox" > /dev/null; then
        echo "✅ Firefox window detected!" | tee -a "$LOG_OUT"
        break
    fi
    sleep 1
done

if ! wmctrl -l | grep -i "Mozilla Firefox" > /dev/null; then
    echo "❌ Error: Firefox window did not appear!" | tee -a "$LOG_ERR"
    exit 1
fi

# Simulate user interaction
echo "🖱️ Simulating user interaction..." | tee -a "$LOG_OUT"
xdotool mousemove 584 81 click 1
sleep 0.5
xdotool type "www.replit.com"
xdotool key Return
sleep 14

echo "✅ open.sh completed successfully!" | tee -a "$LOG_OUT"
exit 0
