#!/bin/bash

# Start Xvfb if it's not already running
if ! pgrep -x "Xvfb" > /dev/null; then
    echo "Starting Xvfb..."
    Xvfb :1 -screen 0 1366x641x16 &
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
LOCK_FILE="/tmp/open_sh.lock"

# Kill any existing open.sh process
echo "Stopping any running instance of open.sh..." | tee -a "$LOG_OUT"

# List all running instances before attempting to kill them
echo "Current running open.sh instances (before kill):" | tee -a "$LOG_OUT"
pgrep -fal "bash open.sh" | tee -a "$LOG_OUT"

for pid in $(pgrep -f "bash open.sh"); do
    echo "Killing open.sh process with PID: $pid" | tee -a "$LOG_OUT"
    kill -9 "$pid"
    sleep 1
done

# Ensure process is completely killed
if pgrep -f "bash open.sh" > /dev/null; then
    echo "❌ ERROR: Failed to terminate open.sh! Checking again..." | tee -a "$LOG_ERR"
    sleep 2
    pgrep -fal "bash open.sh" | tee -a "$LOG_ERR"
    exit 1
fi

# Ensure the lock file is removed before restarting
if [ -f "$LOCK_FILE" ]; then
    echo "⚠️ Lock file found! Removing..." | tee -a "$LOG_OUT"
    rm -f "$LOCK_FILE"
fi

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
