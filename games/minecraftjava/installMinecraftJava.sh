#!/bin/bash

# Create a new user named "debian" with the password "1234567890"
sudo useradd -m debian
echo "debian:1234567890" | sudo chpasswd

# Add the user to the sudo group
sudo usermod -aG sudo debian

# Switch to the new user
su - debian

# Download LinuxGSM script and install Minecraft server
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh mcserver

# Installs game dependencies
sudo nala install bc binutils bsdmainutils bzip2 ca-certificates cpio curl distro-info file gzip hostname jq lib32gcc-s1 lib32stdc++6 netcat-openbsd openjdk-17-jre python3 tar tmux unzip util-linux uuid-runtime wget xz-utils -y

# Install Miencraft Java Server
./mcserver install
