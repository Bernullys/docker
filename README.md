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
        Is an advantage because if we need to update a version, only different layers are downloaded.

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
    When we run an image of an operationg system (like ubuntu image), this will create the container but will automatically stoped because docker it's not design to run OS. 
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


---------------------------------------------------------------------
Module Docker Images (How to create own images).

Why we would create our own image ?
Because the image does not exits on DockerHub.
Or beacause we decided that the app we are developing will be containerize for easier deployment.

How to create my own image?
First we need to understand: what we are continerizing or what application we are creating an image for and how the application is built.

Steps to deploy an application manually: (A Flask application as example)
A set of instructions:
    1. OS - Ubuntu.
    2. Update apt repo.
    3. Install dependencies using apt.
    4. Install Python dependencies using pip.
    5. Copy source code to /opt folder.
    6. Run the web server using "flask" command.
Now we create a docker file using the instructions:
    Create a docker file named Dockerfile.
    Write the file.
    Then run the docker file with: docker build Dockerfile -t docker_user/app_image_tagname.
    To make it available on DockerHub: docker push docker_user/app_image_tagname.
How to create the docker file:
    Is a text file written in a specific format that docker understand.
    Is: INSTRUCTION argument (See the DockerFile on ./DockerImagesModule/FirstImage/DockerFile).

Layered architectureins:
    When docker creates an image it does it by layers. Each line of instruction creates a layer.

What can you containerize ?
Almost all kind of applications.

If I'm inside the directory wich has the Dockerfile, and I want to build the image: docker build -t image_name . (. is necessary which indicates the current directory).


---------------------
Enviroment Variables

We can set variables inside our app to be manupulated withing the command to run a container.
Example: docker run -e VARIABLE=variable_value -d -p 8080:8280 --name name_i_want image_name

We can check which variables are set to manipulate on a running container with:
docker inspect container_name
Go to "Config":{... Env: ["VARIABLE", "VARIABLE2,...]}


-------------------
CMD vs ENTRYPOINT

Commands, arguments and entrypoints.

Some Dockerfile has:
    CMD ["command to run"]
For mysql container:
    CMD ["mysqld"]
Ubuntu uses:
    CMD ["bash"]

We can override the command on the command line to run the container.
We can write the command we want inside the Dockerfile like:
    CMD ["command", "param1"]   this is a json array format.

We can also pass only the parameter on the command line to run the container.
There is where EMTRYPOINT comes to play like:
    ENTRYPOINT ["command"]
    and the parameter can be set on the command line to run the container.
    But the parameter has to specified too.
    So we need to use CMD too. In the Dockerfile:
    CMD["param1"] and that param will be the default one.

Finally if we want to override all the entripoint and the cmd:
    docker run --entrypoint new_entrypoint image_name paramX


--------------------------------------------------------------------------------------------------
Module: Docker Compose.

Docker compose is to run not that simple applications.
Insted of a Dockerfile we need to do configurations in yml files: docker-compose.yml.
Command to run the compose: docker-compose up

There will be several containers and will be compose to work together.
This is only applicable on containers that are running on a single docker host.

Sample application - Voting application:
    First we need to run all the already made images, and we need to named every container to use its name later on.
    If the container will be running a server in a port, that will be the port of the container, and we need to set the port for the host, so we can access from a browser.
    Second we already have all the containers running but we need to link the ones that has to be link. And to do that we use the --link name_container_to_link:name_host_the_container_is_looking  This is why we named the containers.
    Third we can start the compose file. The names of the containers are the keys, and the value is the name of the image to use. Also the other commands will be pass as values.
    There is an option to insted of passing the image value, pass the build: path_of_file_to_create_an_image.

    Docker compose - versions. There are different versions and we can see any of them.
    From version 2 onwards the version is type on top of the docker-compose.yml.
    And from version 2 the link command is not needed anymore.
    Version 3 will be explain later. It supports Docker Swarm.

    Networks:
    Now Docker compose separate frontend (Network 1) and backend (Network 2). And we need to add between the values, if is only frontend, only backend or both.

Demo - Example Voting Application.

    Clone the repository from github:
        git clone git@github.com:dockersamples/example-voting-app.git
    Create an image from vote folder. Is name is voting-app:
        docker build -t voting-app .
    Create a container from voting-app image, and I named it voting-app-container, and is deploy on port 5000:
        docker run -d -p 5000:80 --name voting-app-container voting-app
    Create a container from redis. I hadn't that image so it was bring from dockerHub. But is working, and also is name is redis:
        docker run -d --name redis redis
    I stop the voting-app-container:
        docker stop container_id
    Create an instance of voting app but now link to redis:
        docker run -d -p 5000:80 --link redis:redis voting-app
    Create an image from db. We have to check which version of postgres image was used in the compose file in the repository. Is postgres:15-alpine
    Create an instance of the image named db:
        docker run -d --name db postgres:15-alpine  But is not running that container, got stop right away.
        I ask chat-gpt and give me this command: (I change the name to dbs)
            docker run -d --name dbs \
            -e POSTGRES_USER=admin \
            -e POSTGRES_PASSWORD=secret \
            -e POSTGRES_DB=test_db \
            -p 5432:5432 \
            postgres:15-alpine
    Create an image from worker folder named worker-app:
        docker build -t worker-app .
    Run an instance of the worker-app image but it needs two links, one to the postgres database and another to the redis:
        docker run -d --link redis:redis --link dbs:dbs worker-app
    Next step is build and deploy the resulting app:
    Create an image from the result app:
        docker build -t result-app .
    The result-app is a webserver so it has a port, so we have to set it to an empty port and also we need to link it to the dbs:
        docker run -d -p 5001:80 --link dbs:dbs result-app
    The apo not work for me as spected... But all the images and containers ran as spected.









