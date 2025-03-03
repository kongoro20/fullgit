#!/bin/bash

# List of scripts to run in the specified order
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
  "outlook5.py"
  "outlook6.py"
  "github1.py"
  "github2.py"
  "github3.py"
  "github4.py"
  "test7.py"
  "deleteworkspace.py"
)

# Run the loop 10 times
for ((i=1; i<=10; i++)); do
  echo "Starting loop iteration $i..."
  
  sleep 2  # Delay before starting the scripts

  # Iterate through the scripts
  for script in "${scripts[@]}"; do
    if [[ -f "$script" ]]; then
      echo "Running $script..."
      
      # Set timeout (250s for all scripts except outlook4.py)
      if [[ "$script" == "outlook4.py" ]]; then
        timeout 100s python3 "$script"
      else
        timeout 250s python3 "$script"
      fi

      exit_status=$?

      # Handle timeout cases
      if [[ "$script" == "outlook4.py" && $exit_status -eq 124 ]]; then
        echo "Script $script exceeded 100 seconds. Skipping and continuing..."
        continue  # Skip outlook4.py and proceed with the next script
      elif [[ $exit_status -eq 124 ]]; then
        echo "Script $script exceeded 7 minutes. Exiting main script."
        exit 1
      fi

      # Check if test3.py or test4.py exited with status 100 (VNC detected)
      if [[ ("$script" == "test3.py" || "$script" == "test4.py") && $exit_status -eq 100 ]]; then
        echo "VNC detected in $script, exiting current loop iteration..."
        break
      fi

      echo "Finished $script. Sleeping for 2 seconds..."
      sleep 2
    else
      echo "Script $script not found. Skipping..."
    fi
  done
done

echo "All loops completed."
