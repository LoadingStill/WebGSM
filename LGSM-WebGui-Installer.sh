#!/bin/bash
# run this file with sudo permissions, this will allow creation of needed folders /var/www
# downloading files into that folder and creation of the .service file for running this program at boot

# variables
NEW_USER=$SUDO_USER

# Define ANSI color codes
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

# Define the URL of the file you want to download from Gitea
GITEA_FILE_URL="https://git.howtoit.com/LoadingStill/LGSM-WebGUI/archive/main.zip"

# Make the folder where this will be stored
mkdir /var/www

# Download file to /var/www folder
wget -O /var/www/lgsm-webgui.zip https://git.howtoit.com/LoadingStill/LGSM-WebGUI/archive/main.zip

# Unzip file
unzip /var/www/lgsm-webgui.zip -d /var/www/

# Remove no longer needed zip file
rm /var/www/lgsm-webgui.zip

# Tells user what has completed
echo -e ${GREEN}"Download, unzip, and move completed."${RESET}

# make /var/www/lgsm-webgui/run.sh executable
sudo chmod +x /var/www/lgsm-webgui/run.sh

# Adds user to nologin group
sudo useradd -r -s /bin/nologin $NEW_USER

# Change ownership of file to group lgms-webgui
sudo chown -R $NEW_USER:$NEW_USER /var/www/lgsm-webgui

# Create the systemd service unit file
cat <<EOL > /etc/systemd/system/lgsm-webgui.service
[Unit]
Description=LGMS-WebGUI start at boot.

[Service]
Type=simple
User=$NEW_USER
ExecStart=/var/www/lgsm-webgui/run.sh

[Install]
WantedBy=multi-user.target
EOL

# Reload the systemd manager to recognize the new service
systemctl daemon-reload

# Enable the service to start on boot
systemctl enable lgsm-webgui.service

# Start the service
systemctl start lgsm-webgui.service

echo -e ${GREEN}"Start at boot enabled." ${RESET}