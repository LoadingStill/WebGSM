#!/bin/bash
# This scrip will not remove game servers, you will need to do that manually through the gui or terminal.

# Stop the application from starting at boot
sudo systemctl disable WebGSM.service

# Stop the application from running
sudo systemctl stop WebGSM.service

# Remove the file that allows start at boot
sudo rm /etc/systemd/system/WebGSM.service

# Reload systemctl daemon
sudo systemctl daemon-reload

# Remove the webgui files
sudo rm -r /var/www/WebGSM

# Removed the initial isntall script
sudo rm /$SUDO_USER/Downloads/WebGSM-Installer.sh