#!/bin/sh
# -------------------------------------------------------------
# TTS Loop Runner Script
# -------------------------------------------------------------
# This script runs tts_speak.py in a continuous loop.
# It clears the screen, executes the Python script,
# then shows a live countdown before restarting.
#
# Usage:
#   chmod +x run_tts_loop.sh   # Make script executable
#   ./run_tts_loop.sh          # Run the loop
#
# To stop the script: press Ctrl + C
# -------------------------------------------------------------

PYTHON_SCRIPT="tts_speak.py"
SLEEP_TIME=5

# Check if Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "❌ Error: $PYTHON_SCRIPT not found in current directory."
  exit 1
fi

while true; do
  clear
  echo "🚀 Running $PYTHON_SCRIPT ..."
  python3 "$PYTHON_SCRIPT"

  # Countdown in same line
  count=$SLEEP_TIME
  while [ $count -gt 0 ]; do
    echo -ne "\r⏳ Restarting in $count seconds... "
    sleep 1
    count=$((count - 1))
  done
  echo ""  # move to new line after countdown finishes
done
