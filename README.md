# docker

Docker course overview:

    What is Docker and what is a container.
    Docker vs Virtual Machine.
    Docker Installation.
    Main commands.
    Debugging a container.
    Developing with containers.
    Docker compose - Running multiple services.
    Dockerfile - Building own Docker image.
    Private Docker Repository (AWS).
    Deploying the containerized App.
    Volumes - Persisting data.
    Volumes Demo.

1- What is Docker?

    What is a container and what problems does it solve?
        A way to package application with all the necessary dependencies and configuration.
        Portable artifact, easily shared and moved around.
        Makes development and deployment more efficient.
    Where do containers live? 
        Container Repository.
        Private repositories.
        Public repository for Docker (DockerHub). Got an account.
    
    Application Development:
        Before containers:
            Installation process different on each OS environment.
            Many steps where something could go wrong.
        After containers:
            Own isolated enviroment.
            Packaged with all needed configuration.
            One command to install the app.
            Run same app with 2 different versions.
    Application Deployment:
        Before containers:
            Developers make a file with instructions of dependencies and Operation had to configurate.
            This lead to:
                Configuration on the served needed.
                    Dependency version conflicts.
                Textual guide of deployment:
                    Misunderstandings.
        After containers:
            Developers and Operations work together to package the application in a container.
            No enviromental configuration needed on server. Except Docker Runtime.

    What is a Container (technically)?
        Layers of images.
        Mosly Linux Base Image, because small in size.
        Application image on top.

            pastgres:10.10      Layer - application image
            --------------      Intermedia images
            --------------
            alpine:3.10         Layer - linux base image

        Separate images are downloaded when bringing from DockerHub.
        Is an advantage because if we nedd to update a version, only different layers are downloaded.

    How to differentiate an image from a container:
    
    Docker Image                        Docker Container
    The actual package.                 Actually start the application.
    Like:                               Container environment is created.
    Configuration.                      When is running            
        PostgresSQL v9.3                Is a running enviroment for Image
        Start script                    Virtual file system
    Artifact,                           Port binded: talk to app running inside of container (Port 5000)
    that can be moved around.           Application image: postgres, redis, mongodb,...
        It's not running.

    Docker vs Virtual Machine: Both are vertualization tools
        Docker on OS level.
        Different levels of abstractions.
        Why linux-based docker containers don't run on Windows.

        Docker on OS level:
            OS has two layers:
                Applications    2.Layer     Run on kernel layer
                OS Kernel       1.Layer     Communicates with the hardware 
                Hardware

            Docker virtualize the Application layer and uses the kernal of the host.
            Virtual Machine virtualize the Application and the OS Kernel. 

            Size: Docker image much smaller.
            Speed: Docker containers start and run much fast.
            Compatibility: VM of any OS can run on any OS host. Docker can't do that.

            Windows versions below 10 can't run docker because its kernel is not compatible
            with Linux base applications. But on those cases we can use Docker Toolbox.

    Install Docker:
        Before installing Docker - pre-requisites.
        On Mac
        On Windows
        On Linux
        Docker Toolbox for older Mac and Windows


CONTAINER Port vs HOST Port

A container is a virtual enviroment running in your host.
So multiple containers can run on your host machine.
Your machine have certain ports available.
We will have conflict when same port on host machine.
So we need to bind them to different ports of the host machine.

Example:

Host ports:         Port 5000   Port 3000   Port 3001

Container ports:    Port 5000   Port 3000   Port 3000


Debugging Containers:
    docker logs
    docker exec -it

---------------------------------------------------------------------
Notes from Docker training Course for the Absolute Beginner.


Sharing the kernel: As long as all softwares shares the same OS

    Software1   Software2   Software3   Software4
    ------------Docker---------------------------
    ----------------------OS---------------------

Example: windows can't run on Linux OS. When we have windows and run a Linux base container, actually windows is runing a VM with Linux OS so can have a Linux container on top.

The main object of Docker is to package a containerized applications and to ship them and to run them anywhere, any time and any times as you want.


Containrs vs Virtual Machines:

VM:                                         Container:
    App                                             App
    Libs/Deps                                       Libs/Deps
    OS                                              ---------
    --------                                        Docker    
    Hypervisor                                      ---------
    --------                                        OS
    Hardware Infrastructure                         ---------        
                                                    Hardware Infrastructure

MB                                                  MB
Slow Boot up                                        Faster Boot up                                       

On big projects Containers works with VM.
On these cases multiple Containers run on a VM.


Container vs image:

    Docker Image:               Docker Containers:
    Package                     Instanses of Docker Images running.    
    Template
    Plan

Developers provide Operators with the App and a DockerFile (This is an Image).


Docker Editions:

    Community Edition           Enterprise Edition
    Free Images                 Support, Security, etc... (Pay)


Important:
    When we run an image of an operationg system (like ubuntu image), this will create the container but will automatically stoped because docker it's not designe to run OS. 
    The container will be up only if the app's inside keep active. If those end or crash the container will exit.

    When we pull or run and image from dockerHub: if is official will have only a name, but if is from a user repository will be like user_name/image_name.

-------------------------------------------------
Module Docker Run:

Run -tag:

docker run image_name:image_version     (This is called a tag)
When we don't specificed a tag, will named as latest.

Run - STDIN

Docker runs in a none interactive mode. So if your dockerized app pront for an input, when you run it won't pront normally. So to make it work you must map the container input using -i parameter (for interactive mode).
Example:
docker run -i interactive_image_name
But in this example still we miss the promp.
So if the app promps a message we need the t parameter too. Like:
docker run -it interactive_image_name

Run - PORT mapping (port publishing on containers)

The underline host where docker is installed is called dockerHost or docker engine.
How a user can access my application?
One option is to use the IP asigned to the docker container. But this is an internal IP and would be only accessible withing the docker host.
To get access from outside we could use the IP of the Docker Host but for that to work you have to map the port inside the docker container to a free port on the Docker Host. (Remember the image of the video)
Example:
docker run -p 80:5000 image_name_1
docker run -p 8000:5000 image_name_1
docker run -p 8001:5000 image_name_1
docker run -p 3306:3306 image_name_2
docker run -p 8306:3306 image_name_2
docker run -p 3306:3306 image_name_2    This is an error is going to a Docker Host port that is allready used.

Run - Volume mapping (persisting data on a docker container)

When we stop and remove a container, the data will be deleted.
To keep the data we can do this (example):
docker run -v /opt/datadir:/var/lib/image_name image_name
This way we create a file in the Docker Host but outside the Docker container.

Inspect Container (More details about a container)

docker inspect container_name_or_id
This command will return a json with all data.


Container Logs

docker logs container_name_or_id
Will show the logs of the container.









