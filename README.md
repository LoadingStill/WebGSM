# About WebGSM

Welcome to WebGSM, is a user-friendly web based graphical interface for LinuxGSM (Linux Game Server Managers).  
**DISCLAIMER** - WebSGM and LinuxGSM are not the same project, and in no way is WebGSM an offical or offically supported by LinuxGSM.  This is just my personal project.  
I am waiting on a [reply](https://github.com/GameServerManagers/LinuxGSM/discussions/4371) about use of LinuxGSM name in my project.

## Installation
- Officially Debian 11 is supported.
- Go to this files page [WebGSM-Installer.sh](https://git.howtoit.com/LoadingStill/WebGSM/src/branch/main/WebGSM-Installer.sh) and click the download icon on the top right of the file.
- Change the files permission to allow execution `sudo chmod +x ~/Downloads/WebGSM-Installer.sh`
- Run the file `sudo ~/Downloads/WebGSM-Installer.sh`
- I am working on a more detailed guide for installing WebGSM on the repo wiki, [Installation](https://git.howtoit.com/LoadingStill/WebGSM/wiki/Installation).

## Uninstalling
- Change the files permission to allow execution `sudo chmod +x /var/www/WebGSM/uninstall.sh`
- Run the file `sudo /var/www/WebGSM/uninstall.sh`
- **This will not unisntall the game servers you installed.  You will need to do that manually in the gui or the terminal.  Each game server is running as its own user, delete the user equals deleting the game server.  Please remember to close the ports of the games you remove.

## Project Overview
WebGSM is a passionate endeavor to enhance the experience of managing game servers on Linux using the well-established LinuxGSM toolset. We recognize the importance of efficient server administration, and our goal is to make it accessible to both novices and experienced users alike.

## Key Features
- **User-Friendly Interface:** Say goodbye to complex command-line interactions. Our GUI offers a visually appealing and user-friendly interface that simplifies server management tasks.
- **Seamless Integration:** WebGSM seamlessly integrates with LinuxGSM, harnessing its powerful features while providing a modern graphical layer.
- **Intuitive Controls:** Execute commands, configure settings, and monitor server performance with ease through intuitive controls and organized menus.
- **Real-Time Monitoring:** Keep a close eye on your game servers with real-time monitoring of vital statistics, ensuring a smooth gaming experience for all players.
- **Automatic Updates:** Stay up-to-date effortlessly. WebGSM streamlines the process of updating both the GUI and the underlying LinuxGSM tools.
- **Multi-Server Management:** Manage multiple game servers concurrently from a single centralized interface, optimizing your server administration workflow.

## Contributors
WebGSM is a collaborative effort fueled by a community of passionate gamers, developers, and Linux enthusiasts. Our contributors come from diverse backgrounds, uniting their skills to create an exceptional tool that benefits the gaming community.

Contributor:
- [LoadingStill](https://git.howtoit.com/LoadingStill)


## Get Involved
I invite you to join us on this exciting journey. Whether you're a developer, designer, or simply someone who shares our passion for gaming and Linux, there's a place for you in our community. Contribute your ideas, code, or expertise and help shape the future of WebSGM.

## GitHub Wiki and Issue Tracker
For additional information, tutorials, and resources, please check out our [Gitea Wiki](https://git.howtoit.com/LoadingStill/WebGSM/wiki) section. If you encounter any issues or have suggestions for improvement, please visit the [Issues or Feature Request](https://git.howtoit.com/LoadingStill/WebGSM/issues) section to report them.

## Stay Connected
Stay informed about the latest developments, releases, and announcements by engaging with our GitHub repository. Together, we're revolutionizing game server management with LinuxGSM.

Thank you for being a part of LinuxGSM, where managing Linux game servers is as enjoyable as playing the games themselves. Let's simplify server management and empower gamers worldwide!