# Components of a Dockerfile
The components of a Dockerfile is described in [Docker official Doc](https://docs.docker.com/engine/reference/builder/) 
,in [this github cheatsheet](https://github.com/wsargent/docker-cheat-sheet#dockerfile).


## Table of Contents
- [FROM]()
- [RUN vs CMD]()


## FROM
It is used to get the base image. It's format is:
```shell script
FROM {image-name}:tag
```
Example: `FROM python:3.8`

By default the image is searched in **DockerHub**. If you want to use your own base image from a private registry 
then use the following command format:
```shell script
FROM {docker-repository-location}:tag
```
Example: Let's say you use **AWS ECR** as your Docker registry. To use image from there, add the command 
`FROM 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-custom-base-image:latest`


## RUN vs CMD
- **RUN** gets executed during the **building of the image**
- **CMD** gets executed **when a container is created** from the image

Example of **RUN:** This instruction can be used in [others forms](https://docs.docker.com/engine/reference/builder/#run).
```shell script
RUN apt-get update -y
```
Example of **CMD:** This instruction can be used in [others forms](https://docs.docker.com/engine/reference/builder/#cmd).
```shell script
CMD echo "Hello World...!"
```


## WORKDIR
```shell script
WORKDIR {a-directory-path}
```
When an statement with **WORKDIR** is run, all the commands after this statement will run inside this directory.
