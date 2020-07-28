# Docker Commands
This document contains the common docker command needed often. This'll help the beginner too to know about the basic 
and frequently used docker commands. This doc may update from time to time.


## Table of Contents
- [Use Docker Without sudo Command]()
- [Get Command Help]()
- [Get docker information]()
- [Docker Lifecycle]()
- [Image Commands]()
- [Container Commands]()


## Use Docker Without sudo Command
To achieve this, perform the following steps. 
- Create the docker group, if it is not already.
```shell script
sudo groupadd docker
```
- Add your user to the **docker** group. See more details 
[here](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo).
```shell script
sudo usermod -a -G docker $USER
```
After adding user to **docker** group, you can use all the docker commands without the **sudo**.


## Get Command Help
- To know available command
```shell script
docker --help
```
- For more information on a command
```shell script
docker {COMMAND} --help
```


## Get Docker Information
- To get docker information
```shell script
docker info
```
- To get version related information, run any of the following commands
```shell script
docker --version
docker -v
docker version
```


## Docker Lifecycle
- To check the status of docker:
```shell script
sudo service docker status
```
- To start docker:
```shell script
sudo service docker start
```
- To stop docker:
```shell script
sudo service docker stop
```
If you already add your user to **docker** group, you can omit **sudo** from the above commands.


## Image Commands
#### Get List of Images
- To get list of images present locally
```shell script
docker images
```
#### Run Image and Enter Into the Container
- To run an image and enter into the container in interactive mood via shell
```shell script
docker run -it {IMAGE} bash
``` 


## Container Commands
#### Container Info
- To get list of all containers
```shell script
docker ps -a
```
or
```shell script
docker container ls -a
```
- To get list of **running** containers
```shell script
docker ps
```
#### Remove Container
- To remove a container. User **-f** flag to remove forcefully.
```shell script
docker container rm {container_id}
```
