#!/bin/bash
# run this file with sudo permissions, this will allow creation of needed folders /var/www
# downloading files into that folder and creation of the .service file for running this program at boot

# Installs the needed software
sudo apt install python3-venv gcc python3-dev python3-pip unzip -y
#pip install --no-binary :all: psutil

# variables
NEW_USER=$SUDO_USER

# Define ANSI color codes
# RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

# Define the URL of the file you want to download from Gitea
GITEA_FILE_URL="https://git.howtoit.com/LoadingStill/WebGSM/archive/main.zip"

# Make the folder where this will be stored
mkdir /var/www

# Download file to /var/www folder
wget -O /var/www/WebGSM.zip https://git.howtoit.com/LoadingStill/WebGSM/archive/main.zip

# Unzip file
unzip /var/www/WebGSM.zip -d /var/www/

# Remove no longer needed zip file
rm /var/www/WebGSM.zip

# Tells user what has completed
echo -e "${GREEN}Download, unzip, and move completed.${RESET}"

# Create a virtual environment
python3 -m venv /var/www/WebGSM/venv

# Activate the virtual environment
source /var/www/WebGSM/venv/bin/activate

# Install the psutil module
pip install psutil

# Exit the virtual environment
deactivate

# make /var/www/WebGSM/run.sh executable
sudo chmod +x /var/www/WebGSM/run.sh

# Adds user to nologin group
sudo useradd -r -s /usr/sbin/nologin "$NEW_USER"

# Change ownership of file to group lgms-webgui
sudo chown -R "$NEW_USER:$NEW_USER" /var/www/WebGSM

# Create the systemd service unit file
cat <<EOL > /etc/systemd/system/WebGSM.service
[Unit]
Description=LGMS-WebGUI start at boot.

[Service]
Type=simple
User=$NEW_USER
ExecStart=/var/www/webgsm/run.sh

[Install]
WantedBy=multi-user.target
EOL

# Reload the systemd manager to recognize the new service
systemctl daemon-reload

# Enable the service to start on boot
systemctl enable WebGSM.service

# Start the service
systemctl start WebGSM.service

echo -e "${GREEN}Start at boot enabled. ${RESET}"

# Set the directory where you want to search for .sh files
directory="/var/www/WebGSM"

# Use the find command with sudo to locate all .sh files and make them executable
# This allows execution of all .sh files for game instlation and edditing.
sudo find "$directory" -type f -name "*.sh" -exec sudo chmod +x {} \;