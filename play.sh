#!/bin/bash

if [[ -f "exit_signal.txt" ]]; then
  echo "Exit signal detected in play.sh. Exiting..."
  exit 0
fi

bash setup.sh

# Activate the Python virtual environment
source /root/fullgit/myenv/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
  echo "Failed to activate the virtual environment."
  exit 1
fi

# Prepare environment
touch ~/.Xauthority

# Install required Python packages
pip install pyautogui
pip install --upgrade pillow
pip install opencv-python-headless
pip install pyperclip
sleep 2
while true; do
  bash script1.sh

  if [ $? -eq 0 ]; then
    break  # Exit loop if script1.sh succeeds
  fi

  echo "script1.sh failed. Restarting..."
  sleep 2
done

# Sleep for 2 seconds before starting the next script
sleep 2

if [[ -f "exit_signal.txt" ]]; then
  echo "Exit signal detected in play.sh. Exiting..."
  exit 0
fi

# Run run.sh and wait for it to finish 
bash run.sh
if [ $? -ne 0 ]; then
  echo "run.sh failed, exiting..." 
  exit 1
fi
