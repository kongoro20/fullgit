#!/bin/bash

# Load virtual environment
source myenv/bin/activate

# Get the last created Firefox profile from `current_profile.txt`
if [ ! -f "current_profile.txt" ]; then
    echo "Error: current_profile.txt not found!"
    exit 1
fi

PROFILE_NAME=$(cat current_profile.txt)
PROFILE_DIR="$HOME/.mozilla/firefox/$PROFILE_NAME"

# Check if the profile directory exists
if [ ! -d "$PROFILE_DIR" ]; then
    echo "Error: Firefox profile '$PROFILE_NAME' not found!"
    exit 1
fi

echo "Launching Firefox with profile: $PROFILE_NAME"

# Open Firefox with the profile
nohup firefox --no-remote --new-instance --profile "$PROFILE_DIR" &> /dev/null &

# Wait for Firefox to fully open
sleep 2

# Click on (584, 81) using xdotool
echo "Clicking on (584, 81)..."
xdotool mousemove 584 81 click 1

# Wait before typing
sleep 0.5

# Type "www.replit.com" and press Enter
xdotool type "www.replit.com"
xdotool key Return

# Wait for 14 seconds
sleep 14

echo "Process completed!"
