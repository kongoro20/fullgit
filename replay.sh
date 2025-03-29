#!/bin/bash

sleep 1
source /root/fullgit/myenv/bin/activate  # Explicit path to myenv
export DISPLAY=:1  # Redundant with Supervisor, but ensures manual runs work
export XAUTHORITY=/root/.Xauthority  # Ensure X server access
sleep 2

echo "Starting open.sh..." >> /root/replay_out.log
bash open.sh
if [ $? -ne 0 ]; then
    echo "open.sh failed, exiting..." | tee -a /root/replay_err.log
    exit 1
fi
sleep 6

echo "Starting run.sh..." >> /root/replay_out.log
bash run.sh
run_status=$?  # Capture the exit status of run.sh

# If run.sh fails, run top.sh
if [ $run_status -ne 0 ]; then
    echo "run.sh failed, running top.sh..." | tee -a /root/replay_err.log
    bash top.sh  # Run top.sh if run.sh fails
fi

# If run.sh finished successfully, print the success message
if [ $run_status -eq 0 ]; then
    echo "run.sh completed successfully." >> /root/replay_out.log
fi

echo "replay.sh completed successfully." >> /root/replay_out.log
