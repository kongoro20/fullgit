#!/bin/bash

# Add Mozilla Team PPA for Firefox
sudo add-apt-repository -y ppa:mozillateam/ppa

# Fix broken dependencies
sudo apt -y --fix-broken install

# Update package list
sudo apt update

# Install Firefox and required packages
sudo apt install -y firefox xdotool zip curl jq xclip unzip git python3-dev python3-tk python3-pip gnome-screenshot python3.8-venv supervisor

# Create Python virtual environment in /root/fullgit
python3 -m venv /root/fullgit/myenv

# Activate the virtual environment
source /root/fullgit/myenv/bin/activate

# Ensure .Xauthority file is created
touch ~/.Xauthority
xauth generate :1 .  # Generate Xauth for DISPLAY=:1

# Install Python packages
pip install --upgrade pip
pip install pyautogui pillow opencv-python-headless requests

# Output completion message
echo "All packages installed and environment set up successfully."

# Add Supervisor configuration
sudo bash -c 'cat <<EOF > /etc/supervisor/conf.d/replay.conf
[program:replay_script]
command=/bin/bash -c "cd /root/fullgit && bash replay.sh"
directory=/root/fullgit
autostart=false  # Changed to false to prevent immediate start
autorestart=true
startsecs=20
stderr_logfile=/root/replay_err.log
stdout_logfile=/root/replay_out.log
environment=DISPLAY=:1,XAUTHORITY=/root/.Xauthority
EOF'

# Reload Supervisor to apply changes
sudo supervisorctl reread
sudo supervisorctl update

# Do NOT start the program immediately
# Commenting out the start command
# sudo supervisorctl start replay_script

# Verify Supervisor configuration was added successfully
if [ $? -eq 0 ]; then
    echo "Supervisor configuration successfully added (not started yet)."
else
    echo "Failed to add Supervisor configuration."
    exit 1
fi
