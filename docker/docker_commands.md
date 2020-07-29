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

#### Filter Image
```shell script
docker images -f "{key=value}"
```

#### Get Image Details
```shell script
docker inspect [OPTIONS] {NAME|ID} [NAME|ID...]
```

#### Pull an Image from a Registry
- To pull an image from a private registry, you need to login before pulling or supply credentials at prompt 
after the command is run. 
```shell script
docker pull {image-name or private-registry-location}[:tag]
```
Example: if you want to login to AWS ECR use the following command.
```shell script
aws ecr get-login-password --profile {aws-profile-name} --region {aws-region-name} \
| docker login --username AWS --password-stdin {account-id}.dkr.ecr.{aws-region-name}.amazonaws.com
```

#### Push an Image to the Registry
- To push an image to a registry, you need to login before pulling or supply credentials at prompt 
after the command is run. 
```shell script
docker push [OPTIONS] {NAME}[:TAG]
```
If you want to sign the image use `--disable-content-trust false` as OPTION. By default, the signing is disabled.

#### Run Image
- To run an image, enter the following command. This will create a container.
```shell script
docker run {image-name}
```
- To run an image and enter into the container in interactive mood via shell
```shell script
docker run -it {IMAGE} bash
``` 

#### Remove Image
```shell script
docker rmi [OPTION] {iamge1} [image2...] 
```
To remove an image forcefully, add `-f` or `--force` as OPTION in the above command.


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
or
```shell script
docker container ls
```

#### Start an Stopped Container
- To start an stopped container
```shell script
docker start [OPTIONS] Container1Name/Container1ID [Container2Name/Container2ID...]
```

#### Stop an Stopped Container
- To stop a running container
```shell script
docker stop [OPTIONS] Container1Name/Container1ID [Container2Name/Container2ID...]
```
OPTION `-t` or `--time` can be used as *seconds to wait for stop before killing it (default 10)*.

#### Remove Container
- To remove a container. User **-f** flag to remove forcefully.
```shell script
docker rm [OPTIONS] Container1Name/Container1ID [Container2Name/Container2ID...]
```
OPTIONS:
- -f, --force ==> Force the removal of a running container (uses SIGKILL)
- -l, --link ==> Remove the specified link
- -v, --volumes ==> Remove anonymous volumes associated with the container
