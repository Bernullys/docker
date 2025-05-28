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

