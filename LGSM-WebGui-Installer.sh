#!/bin/bash

# Define the URL of the file you want to download from Gitea
GITEA_FILE_URL="https://git.howtoit.com/LoadingStill/LGSM-WebGUI/archive/main.zip"

# Make the folder where this will be stored
sudo mkdir /var/www

cd ~/Download

wget https://git.howtoit.com/LoadingStill/LGSM-WebGUI/archive/main.zip

sudo mv Downloads/main.zip /var/www/

echo "Download, unzip, and move completed."



# Create the systemd service unit file
cat <<EOL > /etc/systemd/system/lgsm-webgui.service
[Unit]
Description=Download and Install Script for $(whoami)

[Service]
Type=simple
User=$(whoami)
ExecStart=$(pwd)/download_and_install.sh

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
