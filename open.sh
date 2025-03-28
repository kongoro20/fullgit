#!/bin/bash

# Read the expected profile name from the file
PROFILE_NAME=$(cat current_profile.txt | tr -d '[:space:]')

# Find the actual profile directory (matching any random prefix)
PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name "*$PROFILE_NAME" | head -n 1)

if [ -z "$PROFILE_DIR" ]; then
    echo "❌ Error: Firefox profile '$PROFILE_NAME' not found!"
    exit 1
fi

echo "✅ Found Firefox profile: $PROFILE_DIR"

# Open Firefox with the correct profile
nohup firefox --no-remote --new-instance --profile "$PROFILE_DIR" --purgecaches &> /dev/null &

# Wait for Firefox to load
sleep 2

# Click on (584,81) using xdotool
xdotool mousemove 584 81 click 1

# Wait 0.5 seconds
sleep 0.5

# Type 'www.replit.com' and press Enter
xdotool type "www.replit.com"
xdotool key Return

# Wait 14 seconds
sleep 14

echo "✅ Done!"
