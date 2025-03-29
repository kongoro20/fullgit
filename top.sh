#!/bin/bash

for i in {1..30}
do
    echo "Running play.sh - Attempt $i"
    source play.sh
    if [ $? -ne 0 ]; then
      echo "play.sh failed on attempt $i, restarting loop."
      continue  # Restart the loop on failure
    fi
    sleep 2
done

echo "Completed 30 runs of play.sh."
