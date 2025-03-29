#!/bin/bash

LOCK_FILE="/tmp/open_sh.lock"

# Check if another instance is running
if [ -f "$LOCK_FILE" ]; then
    echo "⚠️ Warning: Another instance of open.sh is already running!" | tee -a /root/replay_out.log
    exit 1
fi

# Create lock file
touch "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT  # Ensure lock file is removed on script exit

export DISPLAY=:1
export XAUTHORITY=/root/.Xauthority
export MOZ_DISABLE_RDD_SANDBOX=1  # Fix sandbox issues
export NO_AT_BRIDGE=1  # Prevent accessibility issues

LOG_OUT="/root/replay_out.log"
LOG_ERR="/root/replay_err.log"

echo "Starting open.sh..." | tee -a "$LOG_OUT"

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

# Ensure Firefox is not already running before starting it
if pgrep -fa "firefox.*$PROFILE_NAME" > /dev/null; then
    echo "⚠️ Warning: Firefox is already running!" | tee -a "$LOG_OUT"
else
    echo "Starting Firefox..." | tee -a "$LOG_OUT"
    firefox --no-remote --new-instance --profile "$PROFILE_DIR" --purgecaches > /dev/null 2>> "$LOG_ERR" &
    sleep 3  # Allow time for Firefox to start
fi

# Verify Firefox started successfully
if ! pgrep -fa "firefox.*$PROFILE_NAME" > /dev/null; then
    echo "❌ Error: Firefox failed to start!" | tee -a "$LOG_ERR"
    exit 1
fi

echo "✅ Firefox is running!" | tee -a "$LOG_OUT"

# Simulate user interaction
xdotool mousemove 584 81 click 1
sleep 0.5
xdotool type "www.replit.com"
xdotool key Return
sleep 14

echo "✅ open.sh completed successfully!" | tee -a "$LOG_OUT"
exit 0
