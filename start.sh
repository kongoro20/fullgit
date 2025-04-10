#!/bin/bash

# Handle Ctrl+C and stop all child processes, also create the exit signal file
trap "echo 'Ctrl+C detected in start.sh. Creating exit signal file and stopping all scripts...'; touch exit_signal.txt; kill 0; exit 0" SIGINT

# If exit signal exists, terminate
if [[ -f "exit_signal.txt" ]]; then
  echo "Exit signal detected in start.sh. Exiting..."
  exit 0
fi

scripts=(
  "test1.py"
  "test2.py"
  "test3.py"
  "test4.py"
  "save.py"
  "omocaptcha.py"
  "outlook1.py"
  "outlook2.py"
  "outlook3.py"
  "outlook4.py"
  "github1.py"
  "github2.py"
  "github3.py"
  "github4.py"
  "test7.py"
  "deleteworkspace.py"
)

for ((i=1; i<=50; i++)); do
  echo "Starting loop iteration $i..."
  sleep 2

  for script in "${scripts[@]}"; do
    # Check for exit signal at the start of each iteration
    if [[ -f "exit_signal.txt" ]]; then
      echo "Exit signal detected in start.sh. Exiting..."
      exit 0
    fi

    if [[ -f "$script" ]]; then
      echo "Running $script..."

      # Set timeouts based on the script
      if [[ "$script" == "outlook4.py" ]]; then
        timeout 100s python3 "$script" &
      elif [[ "$script" == "test3.py" ]]; then
        timeout 300s python3 "$script" &
      else
        timeout 250s python3 "$script" &
      fi

      pid=$!  # Store process ID
      wait $pid  # Wait for process to finish

      exit_status=$?

      # Skip timeout error handling for save.py
      if [[ "$script" != "save.py" ]]; then
        # Handle timeout conditions
        if [[ "$script" == "outlook4.py" && $exit_status -eq 124 ]]; then
          echo "Script $script exceeded 100 seconds. Skipping..."
          continue
        elif [[ $exit_status -eq 124 ]]; then
          echo "Script $script exceeded 7 minutes. Exiting."
          exit 1
        fi
      fi

      # Handle VNC detection condition
      if [[ ("$script" == "test3.py" || "$script" == "test4.py") && $exit_status -eq 100 ]]; then
        echo "VNC detected in $script, exiting iteration..."
        break
      fi

      echo "Finished $script. Sleeping..."
      sleep 2
    else
      echo "Script $script not found. Skipping..."
    fi
  done
done

echo "All loops completed."
