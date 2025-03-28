#!/bin/bash

sleep 1
source /root/fullgit/myenv/bin/activate  # Explicit path to myenv
export DISPLAY=:1  # Ensure DISPLAY is set (redundant with Supervisor, but safe)
export XAUTHORITY=/root/.Xauthority  # Ensure X server access
sleep 2

echo "Starting open.sh..." >> /root/replay_out.log
bash open.sh
if [ $? -ne 0 ]; then
    echo "open.sh failed, exiting..." | tee -a /root/replay_err.log
    exit 1
fi
sleep 3

echo "Starting run.sh..." >> /root/replay_out.log
bash run.sh
if [ $? -ne 0 ]; then
    echo "run.sh failed, exiting..." | tee -a /root/replay_err.log
    exit 1
fi

echo "replay.sh completed successfully." >> /root/replay_out.log
