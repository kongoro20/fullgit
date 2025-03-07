#!/bin/bash

# Remove the stop flag at the beginning
rm -f stop_repl2.flag

echo "Running tempmail.py..."
python3 tempmail.py

echo "Running repl1.py..."
python3 repl1.py

# Check if stop flag exists
if [ -f "stop_repl2.flag" ]; then
    echo "Stop flag detected. Stopping script1.sh and exiting..."
    exit 1  # Return an error code so play.sh knows script1.sh failed
fi

echo "Running repl2.py..."
python3 repl2.py

echo "All scripts executed successfully."
