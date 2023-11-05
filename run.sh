#!/bin/bash

# Change to the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Install virtualenv if not already installed
sudo apt install python3-venv

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required versions...
pip install -r "$SCRIPT_DIR/requirements.txt"

# Run the Flask application
python3 "$SCRIPT_DIR/app.py"
