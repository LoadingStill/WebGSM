#!/bin/bash

# Create a new user named "mcserver" with the password "1234567890"
sudo useradd -m mcserver
echo "mcserver:1234567890" | sudo chpasswd

# Add the user to the sudo group
sudo usermod -aG sudo mcserver

# Switch to the new user
su - mcserver

# Installs game dependencies
sudo apt install bc binutils bsdmainutils bzip2 ca-certificates cpio curl distro-info file gzip hostname jq lib32gcc-s1 lib32stdc++6 netcat-openbsd openjdk-17-jre python3 tar tmux unzip util-linux uuid-runtime wget xz-utils -y


# Download LinuxGSM script and install Minecraft server
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh mcserver

# Install Miencraft Java Server
./mcserver install
