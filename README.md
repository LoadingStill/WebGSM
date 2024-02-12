# About WebGSM

Welcome to WebGSM, is a user-friendly web based graphical interface for LinuxGSM (Linux Game Server Managers).  
**DISCLAIMER** - WebSGM and LinuxGSM are not the same project, and in no way is WebGSM an offical or offically supported by LinuxGSM.  This is just my personal project.  
I am waiting on a [reply](https://github.com/GameServerManagers/LinuxGSM/discussions/4371) about use of LinuxGSM name in my project.

## Installation
- Officially Debian 11 is supported.
- Go to this files page [WebGSM-Installer.sh](https://github.com/LoadingStill/WebGSM/raw/branch/main/WebGSM-Installer.sh) and click the download icon on the top right of the file.
  - In a terminal only enviroment use this command `wget -O WebGSM-Installer.sh https://github.com/LoadingStill/WebGSM/raw/branch/main/WebGSM-Installer.sh`
- Change the files permission to allow execution `sudo chmod +x ~/[file location]/WebGSM-Installer.sh`
  - Changes the file to allow execution.
- Run the file `sudo ~/[file location]/WebGSM-Installer.sh`
- I am working on a more detailed guide for installing WebGSM on the repo wiki, [Installation](https://github.com/LoadingStill/WebGSM/wiki/Installation).

## Uninstalling
- Change the files permission to allow execution `sudo chmod +x /var/www/WebGSM/uninstall.sh`
- Run the file `sudo /var/www/WebGSM/uninstall.sh`
- **This will not unisntall the game servers you installed.  You will need to do that manually in the gui or the terminal.  Each game server is running as its own user, delete the user equals deleting the game server.  Please remember to close the ports of the games you remove.

## Project Overview
WebGSM is an easier way of managing game servers on Linux using the well-established LinuxGSM toolset. We recognize the importance of efficient server administration, and our goal is to make it accessible to both novices and experienced users alike.

## Current Progress
### November 8, 2023
![Home Page](https://github.com/LoadingStill/WebGSM/blob/main/.github/ProjectUpdate/Nov-8-2023-Status-Home-Page-Update.png)  
When a game is greyed out it means the game is not installed, I have the code that checks if the json Install = True or Flase.  I am going to have the install script change that file to True. When the homepage is loaded right now every game is checked for installed status.  
![Game Page](https://github.com/LoadingStill/WebGSM/blob/main/.github/ProjectUpdate/Nov-8-2023-Status-Home-Page-Update.png) 
Currently the layout is as seen in the image, I plan to have a terminal in the right middle of the screen that will loginto the user that the game server is under.  All game servers will be under a different user to make it easier to maintain servers.


## Key Features
- **User-Friendly Interface:** Say goodbye to complex command-line interactions.
- **Real-Time Monitoring:** Keep a close eye on your game servers with real-time monitoring of vital statistics, ensuring a smooth gaming experience for all players.

## Contributors
WebGSM is a collaborative effort fueled by a community of passionate gamers, developers, and Linux enthusiasts. Our contributors come from diverse backgrounds, uniting their skills to create an exceptional tool that benefits the gaming community.

Contributor:
- [LoadingStill](https://github.com/LoadingStill)


## Get Involved
I invite you to join us on this exciting journey. Whether you're a developer, designer, or simply someone who shares our passion for gaming and Linux, there's a place for you in our community. Contribute your ideas, code, or expertise and help shape the future of WebSGM.

## GitHub Wiki and Issue Tracker
For additional information, tutorials, and resources, please check out our [WebGSM Wiki](https://github.com/LoadingStill/WebGSM/wiki) section. If you encounter any issues or have suggestions for improvement, please visit the [Issues or Feature Request](https://github.com/LoadingStill/WebGSM/issues) section to report them.

## Stay Connected
Stay informed about the latest developments, releases, and announcements by engaging with our GitHub or the [Github](https://github.com/LoadingStill/WebGSM) repository. The Github repo is a mirror of this repository, so replies to the Github one will be slower.
