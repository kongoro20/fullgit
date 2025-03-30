#!/bin/bash

# Start Xvfb if it's not already running
if ! pgrep -x "Xvfb" > /dev/null; then
    echo "Starting Xvfb..."
    Xvfb :1 -screen 0 1366x768x16 &
    sleep 2
fi

# Activate the environment and set necessary variables
sleep 1
source /root/fullgit/myenv/bin/activate  # Explicit path to myenv
export DISPLAY=:1  # Ensures Firefox uses the correct display
export XAUTHORITY=/root/.Xauthority  # Ensure X server access

# Wait for Xvfb to initialize
sleep 2

LOG_OUT="/root/replay_out.log"
LOG_ERR="/root/replay_err.log"

echo "Starting open.sh..." | tee -a "$LOG_OUT"

# Run open.sh and wait for it to complete
bash open.sh
open_status=$?  # Capture the exit status of open.sh

if [ $open_status -ne 0 ]; then
    echo "❌ open.sh failed, exiting..." | tee -a "$LOG_ERR"
    exit 1
fi

echo "✅ open.sh completed successfully!" | tee -a "$LOG_OUT"

# Add an extra delay to ensure Firefox is fully ready
sleep 5  

echo "Starting run.sh..." | tee -a "$LOG_OUT"
bash run.sh
run_status=$?  # Capture the exit status of run.sh

# If run.sh fails, run top.sh
if [ $run_status -ne 0 ]; then
    echo "❌ run.sh failed, running top.sh..." | tee -a "$LOG_ERR"
    bash top.sh  # Run top.sh if run.sh fails
fi

# If run.sh finished successfully, print the success message
if [ $run_status -eq 0 ]; then
    echo "✅ run.sh completed successfully." | tee -a "$LOG_OUT"
fi

echo "✅ replay.sh completed successfully." | tee -a "$LOG_OUT"
exit 0
