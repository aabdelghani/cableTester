#!/bin/bash

# Base directory for the project
BASE_DIR="$(dirname "$0")"

# Path to your main Python script
SCRIPT="$BASE_DIR/src/main.py"

# Log file location
LOG="$BASE_DIR/logs/log.txt"

# Wait for the network to stabilize (optional, adjust time as needed)
sleep 30

# Run the script and redirect output to the log file
sudo /usr/bin/python $SCRIPT >$LOG 2>&1 | tee -a $LOG

