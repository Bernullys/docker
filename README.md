# docker

Docker course overview:

    What is Docker and what is a container.
    Docker vs Virtual Machine.
    Docker Installation.
    Main commands.
    Debugging a container.
    Developing with contaainers.
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

