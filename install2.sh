#!/bin/bash
# Activate the virtual environment
source /var/www/lgsm-webgui/venv/bin/activate

# Install the psutil module
pip install psutil

# Exit the virtual environment
deactivate

exit