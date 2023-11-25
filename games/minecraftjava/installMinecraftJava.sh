#!/bin/bash

adduser mcserver

su - mcserver

wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh mcserver

./mcserver install