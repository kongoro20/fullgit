#!/bin/bash

# Add Mozilla Team PPA for Firefox
sudo add-apt-repository -y ppa:mozillateam/ppa

# Fix broken dependencies
sudo apt -y --fix-broken install

# Update package list
sudo apt update

# Install Firefox and required packages
sudo apt install -y firefox xdotool zip curl jq xclip unzip git python3-dev python3-tk python3-pip gnome-screenshot python3.8-venv

# Create Python virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Ensure .Xauthority file is created
touch ~/.Xauthority

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
autostart=true
autorestart=true
startsecs=10
stderr_logfile=/root/replay_err.log
stdout_logfile=/root/replay_out.log
environment=DISPLAY=:1
EOF'

# Reload Supervisor to apply changes
sudo supervisorctl reread
sudo supervisorctl update

# Start the Supervisor program
sudo supervisorctl start replay_script

# Verify if Supervisor configuration was added successfully
if [ $? -eq 0 ]; then
    echo "Supervisor configuration successfully added and started."
else
    echo "Failed to add or start Supervisor configuration."
    exit 1
fi
