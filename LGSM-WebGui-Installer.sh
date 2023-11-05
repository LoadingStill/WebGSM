#!/bin/bash
# run this file with sudo permissions, this will allow creation of needed folders /var/www
# downloading files into that folder and creation of the .service file for running this program at boot


# Define the URL of the file you want to download from Gitea
GITEA_FILE_URL="https://git.howtoit.com/LoadingStill/LGSM-WebGUI/archive/main.zip"

# Make the folder where this will be stored
mkdir /var/www

wget -O /var/www/file.zip https://git.howtoit.com/LoadingStill/LGSM-WebGUI/archive/main.zip

unzip /var/www/main.zip /var/www/

echo "Download, unzip, and move completed."



# Create the systemd service unit file
cat <<EOL > /etc/systemd/system/lgsm-webgui.service
[Unit]
Description=Download and Install Script for $(whoami)

[Service]
Type=simple
User=$SUDO_USER
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

echo "Setup completed."
