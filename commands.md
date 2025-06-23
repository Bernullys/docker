docker ps               To see all the running containers.
docker ps -a    list running and stopped containers.
docker pull image_name      Only pull it.
docker start container_id
docker stop container_id
docker logs container_id    will show the logs of the running container.
docker images   Show the images ypu have.
docker run image_name   pulls image and starts container right away
docker run -d image_name    Run detached mode
docker attach container_id      To go to attach mode of a running container.
docker run -p 6000:6379  image_name    To bind to a specific port. 6000 is the host and 6379 is the container.
docker run -d -p500:3000 --name the_name_I_want image_name  to create a container with a name we want.
docker exec -it container_id /bin/bash  this is to go inside the running container and from there we can manipulate. To exit just type exit.
docker run -it os_image_name bash       This will send me to the bash terminal of that os image.

Recap: docker run is to create a new container and docker start is to restard an existing container.

Note: We have to stop containers before deleting them.

Note: to modify a text file on the terminal I can use: nano file_name

docker rm container_name or id
docker container prune      Remove all stoped containers.
docker rmi image_name_or_image_id      Remove an image.
docker image prune          
docker image prune --all    Delete all images

docker --help       Will display all commons commands.

docker run image_name sleep 5   To run the container for a defined time (5 seconds in this example).

Exercice:
docker ps --filter ancestor=image_name --format '{{.ID}}'   To identify a container id.
docker exec -it <container id> bash     To interact with the terminal.
echo "This is the file" >> /root/learning.txt   Creates a file and add some text.

docker history image_name   will show the size of each layer of Instructions of the DockerFile.

docker run image_name cat /etc/*release*    Show details of release.