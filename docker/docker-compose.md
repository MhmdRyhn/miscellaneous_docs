# Docker Compose
Docker compose file is used to run a collection of docker containers at a time with some config file 
written in YAML extension.

## Commands For docker-compose.yml File
- If any environment variable is used, to know the real value when the docker compose file is run, 
use the following command:
```shell script
docker-compose config
```
This command will not run the compose file but will print the compose file with real value.

- To run a docker compose file:
```shell script
docker-compose up -d
```
Here `-d` is used to run in detached mode.

- To stop the container
```shell script
docker-compose stop
```

- To stop and remove the container 
```shell script
docker-compose down
``` 
It'll stop the container and then remove the container.

- To stop and remove the container and then remove the data volumes too
```shell script
docker-compose down --volumes
```

