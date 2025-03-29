#!/bin/bash

# Function to handle Ctrl+C (SIGINT)
cleanup() {
  echo "Ctrl+C detected. Creating exit signal file..."

  # Create the exit signal file to stop all scripts
  touch exit_signal.txt

  # Optional: Give it a brief moment before the script exits
  sleep 1
  
  # Exit after creating the exit signal file
  exit 0
}

# Trap SIGINT (Ctrl+C) and run cleanup()
trap cleanup SIGINT

# Repeat the cycle 20 times
for ((i=1; i<=20; i++)); do
  echo "Starting iteration $i of main loop..."

  # Check for exit signal before running anything
  if [[ -f "exit_signal.txt" ]]; then
    echo "Exit signal detected in run.sh. Exiting..."
    exit 0
  fi

  # Run retry.py first
  echo "Running retry.py to check for shutdown button..."
  sleep 5
  python3 retry.py
  if [ $? -ne 0 ]; then
    echo "Failure detected in retry.py. Exiting iteration $i..."
    exit 1  # Exit the iteration and cause failure in play.sh
  fi

  # Run start.sh in the background
  echo "Running start.sh..."
  bash start.sh &
  start_pid=$!
  wait $start_pid
  echo "start.sh finished."

  # Check for exit signal again
  if [[ -f "exit_signal.txt" ]]; then
    echo "Exit signal detected after start.sh. Exiting..."
    exit 0
  fi

  # Sleep before running startagain.py
  sleep 1.5

  # Run startagain.py in the background
  echo "Running startagain.py..."
  python3 startagain.py &
  startagain_pid=$!
  wait $startagain_pid
  echo "startagain.py finished."

  # Check for exit signal again
  if [[ -f "exit_signal.txt" ]]; then
    echo "Exit signal detected after startagain.py. Exiting..."
    exit 0
  fi

  sleep 2
  python3 deleteworkspace.py & 
  deleteworkspace_pid=$!
  wait $deleteworkspace_pid

  # Check for exit signal again
  if [[ -f "exit_signal.txt" ]]; then
    echo "Exit signal detected after deleteworkspace.py. Exiting..."
    exit 0
  fi

  sleep 2
done

echo "All 20 iterations completed."
