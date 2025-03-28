#!/bin/bash
sleep 1
source myenv/bin/activate
sleep 2

bash open.sh
if [ $? -ne 0 ]; then
  echo "open.sh failed, exiting..."
  exit 1
fi
sleep 3

bash run.sh
if [ $? -ne 0 ]; then
  echo "setup.sh failed, exiting..."
  exit 1
fi
