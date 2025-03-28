#!/bin/bash

sleep 1
source myenv/bin/activate
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
