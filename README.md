# Update 28 Dec 2024
I am still working on this project, but I am changing it A LOT.
I am working on learning docker and running this in docker containers instead of just nationally.
I was struggling a lot in making an API that would work properly from my lack of what I know and feature creep.


THIS IS AN ALPHA SOFTWARE!


1. Build the container: `docker build -t webgsm .`
2. Run the Container: `docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock webgsm`
3. Access the Web App: Open a browser and go to `http://localhost:5000/frontend/index.html`

Notes:
The `-v /var/run/docker.sock:/var/run/docker.sock` part allows the container to manage Docker on the host. This is powerful but risky—use with care.



Dockerfile  
/app  
are the new files and folder  

All the other files are the older versions. They will be put in the /app folder eventually


Look into importing docker-compose file from:
https://github.com/GameServerManagers/docker-gameserver/tree/main/docker-compose
If the work is already done, build on top of it, no need to remake the wheel.


For dev use:
1. `python3 -m venv venv`
2. `pip freeze > requirements.txt`