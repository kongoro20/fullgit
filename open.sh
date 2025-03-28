#!/bin/bash

# Read the expected profile name from the file
PROFILE_NAME=$(cat current_profile.txt | tr -d '[:space:]')

# Find the actual profile directory (matching any random prefix)
PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name "*$PROFILE_NAME" | head -n 1)

if [ -z "$PROFILE_DIR" ]; then
    echo "❌ Error: Firefox profile '$PROFILE_NAME' not found!" | tee -a /root/replay_err.log
    exit 1
fi

echo "✅ Found Firefox profile: $PROFILE_DIR" >> /root/replay_out.log

# Open Firefox with the correct profile
nohup firefox --no-remote --new-instance --profile "$PROFILE_DIR" --purgecaches &>> /root/replay_out.log &

# Wait for Firefox to load
sleep 2

# Click on (584,81) using xdotool
xdotool mousemove 584 81 click 1 >> /root/replay_out.log 2>> /root/replay_err.log

# Wait 0.5 seconds
sleep 0.5

# Type 'www.replit.com' and press Enter
xdotool type "www.replit.com" >> /root/replay_out.log 2>> /root/replay_err.log
xdotool key Return >> /root/replay_out.log 2>> /root/replay_err.log

# Wait 14 seconds
sleep 14

echo "✅ Done!" >> /root/replay_out.log
