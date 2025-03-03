#!/bin/bash

# Repeat the cycle 20 times
for ((i=1; i<=20; i++)); do
  echo "Starting iteration $i of main loop..."

  # Run start.sh and wait for it to finish
  echo "Running start.sh..."
  bash start.sh
  echo "start.sh finished."

  # Sleep 1.5 seconds before running startagain.py
  sleep 1.5

  # Run startagain.py and wait for it to finish
  echo "Running startagain.py..."
  python3 startagain.py
  echo "startagain.py finished."
  sleep 2
  python3 deleteworkspace.py
  
  # Sleep 2 seconds before next iteration
  sleep 2
done

echo "All 20 iterations completed."
