#!/bin/bash

LOCK_FILE="/tmp/open_sh.lock"
LOG_OUT="/root/replay_out.log"
LOG_ERR="/root/replay_err.log"
MAX_RETRIES=10
RETRY_DELAY=5

if [ -f "$LOCK_FILE" ]; then
    echo "⚠️ Warning: Another instance of open.sh is already running!" | tee -a "$LOG_OUT"
    exit 1
fi
touch "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

export DISPLAY=:1
export XAUTHORITY=/root/.Xauthority
export MOZ_DISABLE_RDD_SANDBOX=1
export NO_AT_BRIDGE=1
export MOZ_GL_ALWAYS_SOFTWARE=1
export MOZ_NO_SOUND=1
export MOZ_DISABLE_GMP_SANDBOX=1
export MOZ_DISABLE_A11Y=1

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
    echo "🔄 Creating a new Firefox profile..."
    firefox --no-remote --createprofile "newprofile"
    PROFILE_NAME="newprofile"
    PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name "*$PROFILE_NAME*" | head -n 1)

    if [ -z "$PROFILE_DIR" ]; then
        echo "❌ Failed to create a new profile!" | tee -a "$LOG_ERR"
        exit 1
    fi
fi

echo "✅ Found profile: $PROFILE_DIR" | tee -a "$LOG_OUT"

# **🔥 New Fix: Prevent "Troubleshoot Mode" Prompt**
echo 'user_pref("browser.tabs.warnOnClose", false);' >> "$PROFILE_DIR/user.js"
echo 'user_pref("browser.sessionstore.resume_from_crash", false);' >> "$PROFILE_DIR/user.js"
echo 'user_pref("toolkit.startup.max_resumed_crashes", -1);' >> "$PROFILE_DIR/user.js"
echo 'user_pref("app.update.auto", false);' >> "$PROFILE_DIR/user.js"
echo 'user_pref("app.update.enabled", false);' >> "$PROFILE_DIR/user.js"
echo 'user_pref("browser.disableResetPrompt", true);' >> "$PROFILE_DIR/user.js"

# Retry mechanism for opening Firefox
for attempt in $(seq 1 $MAX_RETRIES); do
    echo "🔥 Attempting to start Firefox, attempt $attempt of $MAX_RETRIES..." | tee -a "$LOG_OUT"
    firefox --no-remote --new-instance --profile "$PROFILE_DIR" --display=:1 > /dev/null 2>> "$LOG_ERR" &
    sleep 3

    # Check if Firefox process is running
    if pgrep -fa "firefox.*$PROFILE_NAME" > /dev/null; then
        echo "✅ Firefox process detected!" | tee -a "$LOG_OUT"
        break
    fi

    echo "❌ Firefox did not start. Cleaning caches and retrying..." | tee -a "$LOG_ERR"
    pkill -f firefox
    sleep 2
    rm -rf "$PROFILE_DIR/cache2"
    sleep $RETRY_DELAY
done

# Ensure Firefox window is visible
echo "⏳ Waiting for Firefox window..." | tee -a "$LOG_OUT"
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
