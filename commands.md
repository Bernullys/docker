docker ps               To see all the running containers.
docker ps -a    list running and stopped containers.
docker pull image_name
docker start container_id
docker stop container_id
docker logs container_id    will show the logs of the running container.
docker images   Show the images ypu have.
docker run image_name   pulls image and starts container right away
docker run -d image_name    Run detached mode
docker run -p6000:6379  image_name    To bind to a specific port. 6000 is the host and 6379 is the container.
docker run -d -p500:3000 --name the_name_I_want image_name  to create a container with a name we want.
docker exec -it container_id /bin/bash  this is to go inside the container and from there we can manipulate. To exit just type exit.

Recap: docker run is to create a new container and docker start is to restard an existing container.


