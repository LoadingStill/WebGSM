#!/bin/bash

# Define the URL of the file you want to download from Gitea
GITEA_FILE_URL="https://git.howtoit.com/LoadingStill/LGSM-WebGUI/archive/main.zip"

# Define the destination directory
DESTINATION_DIR="/var/www"

# Define the name of the install script
INSTALL_SCRIPT="install.sh"

# Download the file from Gitea and save it to a temporary location
TMP_DIR=$(mktemp -d)
curl -L -o "$TMP_DIR/downloaded_file.zip" "$GITEA_FILE_URL"

# Unzip the downloaded file
unzip "$TMP_DIR/downloaded_file.zip" -d "$TMP_DIR"

# Move the unzipped files to the destination directory
mv "$TMP_DIR"/* "$DESTINATION_DIR"

# Change the permissions of the install.sh file
chmod +x "$DESTINATION_DIR/$INSTALL_SCRIPT"

# Clean up the temporary directory
rm -rf "$TMP_DIR"

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
