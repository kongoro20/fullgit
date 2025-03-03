#!/bin/bash
bash setup.sh

# Activate the Python virtual environment
source ./myenv/bin/activate

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
bash script1.sh
sleep 2
bash run.sh
