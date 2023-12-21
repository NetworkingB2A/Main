
## Docker
What is docker?  
Docker is a containerization platform. You can take your application and run it on any OS that can run docker. Docker image will consist of all the componants you need to run an application. Docker also helps with tools to manage your containers.

### Understanding Docker
Docker containers use two capabilities in the linux kernel:  
#### Namespaces
Namespaces are essential for providing isolation for containers. Six namespaces are used for this purpose
- mnt (mountpoints): This namespace is used for mapping access to host operating system storage resources to the container process.
- pid (processes): This namespace is used to create a new process ID for an application.
- net (network): This namespace is responsible for network access and mapping communication ports.
- ipc (System V IPC): Inert-process communications controls how the application can access shared memory locations between applications within containers.
- uts (hostname): This namespace controls host and domain names, allowing unique values per process.
- user (UIDs): This namespace is used to map unique user rights to processes
#### Cgroups
Cgroups or control groups are used to mange resource consumption for each container. These values can be tweaked to limit how much resources a container can use at one time.

#### Docker Architecture
The docker engine is the central component of the docker architecture. Docker architecture consists of three primary parts: the client, the docker host and the docker registry.
- The client is a command-line utility that talks to the REST API of the Docker daemon. The client can communicate to a local or remote docker instance.
- The Docker host is where the Docker daemon resides. The Docker daemon is a service that runs on the host operating system.
- The registry is a place to store container images; it is also known as the repository for the container infrastructure. 

#### Using Docker

<b>Working with containers</b>
When working with containers, the key commands are as follows:
- create: Create a container from an image
- start: start an existing container
- run: create a new container and start it.
- ls: list running containers.
- inspect: get detailed information regarding the container.
- logs: Print run logs from the containers's execution.
- stop: Gracefully stop running the container.
- kill: Stop the main process in the container abruptly.
- rm: Delete a stopped container.

<b>Dockerfiles</b>
A Dockerfile is a script that is used to create a container image to your specification. A Dockerfile is simply a text file with a structured set of commands that Docker executes while building this image. Some of the most common commands are as follows:
- FROM: Selects the base image used to start the build process or can be set to scratch to build a totally new image.
- MAINTAINER: Lets you select a name and email address for the image creator.
- RUN: creates image layers and executes commands within a container.
- CMD: Executes a single command within a container. Only one can exist in a Dockerfile.
- WORKDIR: Sets the path where the command defined with the CMD is to be executed.
- ENTRYPOINT: Executes a default application every time a container is created with the image.
- ADD: Copies the files from the local host or remotely via a URL into the container's file system.
- ENV: Set environment variables within the container.
- EXPOSE: Associates a specific port for network binding.
- USER: Sets the UID for a user that is to run the container.
- VOLUME: Sets up shareable directory that can be mapped to a local host directory.
- LABEL: Provides a label to identify the created Docker image.

<b>Docker Images</b>
When working with Docker images, you primarily use the following commands:
All start with commands start with "docker image"
- build: Builds an image form Dockerfile.
- push: Pushes a local image to an remote registry for storage and sharing.
- ls: List images stored locally.
- images: This will show a list of the local docker images.
- history: Shows the creating and build process for an image.
- inspect: Provides detailed information on all aspects of an image, including layer detail.
- rm: Deletes an image from local storage.


Actually building a docker file
- Create the docker file
- run the following command "docker build  -t dockerfile:latest ."
- run the docker container with the following command "docker run -d -p 5000:5000  dockerfile"

Here is an example of a simple dockerfile  
```docker
FROM ubuntu:18.04  
MAINTAINER Adam Angell  
RUN apt-get update -y && apt-get install -y   python3-pip python3-dev  
CMD [ "ufw allow 5000" ]  
COPY ./requirements.txt /app/requirements.txt  
WORKDIR /app  
RUN pip3 install -r requirements.txt  
COPY  ./myAPI.py /app  
ENTRYPOINT [ "python3" ]  
CMD [ "myAPI.py" ]  
```


Steps to add container to the dockerhub  
```
docker tag "image ID"  "name of dockerhub repo":latest  
docker push "name of dockerhub repo"
```
