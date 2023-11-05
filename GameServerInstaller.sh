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
