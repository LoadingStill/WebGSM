#!/bin/bash
# run this file with sudo permissions, this will allow creation of needed folders /var/www
# downloading files into that folder and creation of the .service file for running this program at boot

# Installs the needed software
sudo apt update
sudo apt install python3-venv gcc python3-dev python3-pip unzip curl nala -y
sudo dpkg --add-architecture i386
sudo nala update
#pip install --no-binary :all: psutil

# variables
NEW_USER=$SUDO_USER

# Define ANSI color codes
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

# Make the folder where this will be stored
sudo mkdir /var/www

# Download file and unzip into /var/www folder
wget https://git.howtoit.com/LoadingStill/WebGSM/archive/main.zip -O /tmp/main.zip && sudo unzip /tmp/main.zip -d /var/www/


# Tells user what has completed
echo -e "${GREEN}Download, unzip, and move completed.${RESET}"


# make /var/www/WebGSM/run.sh executable
sudo chmod +x /var/www/webgsm/run.sh

# Adds user to no-login group
sudo useradd -r -s /usr/sbin/nologin "$NEW_USER"

# Change ownership of file to group lgms-webgui
sudo chown -R "$NEW_USER:$NEW_USER" /var/www/webgsm


# Create the systemd service unit file
cat <<EOL > /etc/systemd/system/webgsm.service
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
sudo systemctl daemon-reload

# Enable the service to start on boot
sudo systemctl enable webgsm.service

# Start the service
sudo systemctl start webgsm.service

echo -e "${GREEN}Start at boot enabled. ${RESET}"

# Set the directory where you want to search for .sh files
directory="/var/www/webgsm"

# Use the find command with sudo to locate all .sh files and make them executable
# This allows execution of all .sh files for game installation and editing.
sudo find "$directory" -type f -name "*.sh" -exec sudo chmod +x {} \;

# Sets files in webgsm directory to run sudo commands with out passwords
echo '# Sets script to not need a password to install.  This is only for the webgsm files.' | sudo tee -a /etc/sudoers
echo "$SUDO_USER ALL=(ALL) NOPASSWD: /bin/bash /var/www/webgsm/**/*.sh" | sudo tee -a /etc/sudoers
