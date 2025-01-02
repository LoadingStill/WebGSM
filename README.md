# Update 28 Dec 2024
I am still working on this project, but I am changing it A LOT.
I am working on learning docker and running this in docker containers instead of just nationally.
I was struggling a lot in making an API that would work properly from my lack of what I know and feature creep.
I plan on over explaining everything here so those who would not know the basics can join in as well.

# THIS IS AN ALPHA SOFTWARE!

# Install Info
I plan on adding a section to the git wiki on installing and running WebGSM.

## Download and Run
1. Debian 12: `wget -O docker-compose.yml https://raw.githubusercontent.com/LoadingStill/WebGSM/refs/heads/main/docker-compose.yml`
2. To run in the background: `docker compose up -d` - To run in the forground: `docker compose up`
3. Access the Web App: Open a browser and go to `http://localhost:5050/frontend/index.html`

## Build and Run
1. `git clone https://github.com/LoadingStill/WebGSM.git`
2. Build the container: `docker build -t webgsm .`
3. Run the Container: `docker run -d -p 5050:5050 -v /var/run/docker.sock:/var/run/docker.sock webgsm`
4. Access the Web App: Open a browser and go to `http://localhost:5050/frontend/index.html`
5. OR if you have it local and you want to use this you can: `docker-compose -f docker-compose-dev.yml up`

Notes:
The `-v /var/run/docker.sock:/var/run/docker.sock` part allows the container to manage Docker on the host. This is powerful but risky—use with care.


##  Dev Info


Dockerfile  
/app  
are the new files and folder  

All the other files are the older versions. They will be put in the /app folder eventually


Look into importing docker-compose file from:
https://github.com/GameServerManagers/docker-gameserver/tree/main/docker-compose
If the work is already done, build on top of it, no need to remake the wheel.


### For dev use:
1. `python3 -m venv venv`
2. `pip freeze > requirements.txt`

### Docker compose info
1. set variables in `.env`
2. run `docker-compose up` or `docker-compose up -d` for background run
3. `docker ps --format "{{.ID}}: {{.Image}} - {{.Ports}}"` to see docker contaienr info, docker-compose does not show this info in docker desktop when ran from docker compoase for some reason...

### Links To Learn From
1. https://hub.docker.com/r/gameservermanagers/gameserver
2. https://docs.docker.com/engine/storage/