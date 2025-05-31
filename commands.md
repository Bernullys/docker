docker ps               To see all the running containers.
docker ps -a    list running and stopped containers
docker pull image_name
docker start container_id
docker stop container_id
docker exec -it
docker logs
docker images
docker run image_name   pulls image ans starts container right away
docker run -d image_name    Run deatach mode
docker run -p6000:6379  image_name    To bind to a specific port. 6000 is the host and 6379 is the container.
