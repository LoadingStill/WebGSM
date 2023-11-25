#!/bin/bash

# Sudo code/actual code for installing MCJava server

#add mcserver user requires sudo, requires password to be typed
sudo adduser mcserver

#add new user to sudo group for install to automate the process more
sudo usermod -aG sudo mcserver

#login as mcserver user, requires password to be typed
su - mcserver

#Installs LinuxGSM and installs minecraft java server.
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh mcserver

# Installs game dependencies
sudo nala install bc binutils bsdmainutils bzip2 ca-certificates cpio curl distro-info file gzip hostname jq lib32gcc-s1 lib32stdc++6 netcat-openbsd openjdk-17-jre python3 tar tmux unzip util-linux uuid-runtime wget xz-utils -y

#Installs
./mcserver install