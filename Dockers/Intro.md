- What is Dockers ??
- What are Containers ??
- Containers Vs Virtual Machines
- Docker Image Vs Containers
- Practical Implementation of Dockers
- How we can Dockerize our web application or any application and then run it as a container in any specific cloud, how to convert docker image into docker hub repository. Docker eases the deployment process.

## What problem we face while development and deployment when we are not using containers ??
- Suppose a developer A creating a data science application , installing libraries on windows for it . Let's say tommorow some other developer joins my team and he/she is using some linux/mac/windows machine . Now when developer B joins 1st thing to be done is installation of all the libraries required . Let's say bcoz of some libraries mismatch/dependencies installation doesn't goes well for developer B . Then in this case whatever application developer A would have created will not work on developer B system. Then developer A helper developer B with installation and then everything is working fine . Let's say this development team has now created a developer environment , and from this they have implemented some of the stories , now they have to send this entire application to the QA environment so that testing will start. -> Sending to a QA server. Now in order to setup this QA server again we have to do library installation process , then there was another team setting up the configuration and they missed some of the installation and configuration.-> Then the entire application may not work or some of the modules may not work. Then QA will complain that ur application is not working on our server and it will lead to misunderstanding. These types of issues used to happen before using containers. Whenever we needed to move/deplot our application in other environment , we had to install all the configurations and dependencies manually. This is major issue bcoz team who is doing this setup may miss some of the libraries/configurations.

## What happens when we use containers ?? How is the above issue fixed ??
- What are Containers ?? : Containers are nothing but it is a way to package applications with all the necessary dependencies and configurations.
- This package has a very important property : Its a portable artifact. Portable artifact means we will be able to easily share and move this package to any environment.
- This makes the development and deployment more easy and efficient and in sync.

## Example of Containers
- Let's say u are staying in a house A this is a rented house , then u suddenly buy a news house this is house B , then u need to shift from house A to house B. House A has many items present over there to shift to B it won't be feasible to take each item at a time go and put it at house B and then come back(there are chances that u may miss some of the items). What we do is take all the items(from A)and put it in a container i.e u are packaging it , then put the container in a big vechicle and shift it over the house B , there u will unpack it and place all the items back to ur house B.

- This is the same concept w.r.t containers also , suppose u are developing a application , whatever dependencies u have it in this application , u will try to put all the dependencies over there (in container) in form of base image in multiple layers. -> This will be packaged as a container. From dev environment its packaged as a container , we will take the same container and go to the QA environment and i can run this container on QA environment with all the dependencies.

- It will run similiar to how it used to run in Dev environment

- We can take the same container and do the same for the production environment also. Take the container to the production environment and run it over there. Bcoz of this there will be no issues related to dependencies or packages -> Why ?? -> Bcoz we have already containerized all the dependencies.

## What is Docker ??
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code, you can significantly reduce the delay between writing code and running it in production.

## Docker Image and Configurations
- Suppose u have a application and this application has lot of dependencies and configurations , inorder to convert this application into a container what we have to do is we have to containerize/dockerize this entire application. In terms of container what we basically do is that we create layers of images (multiple layers of images).
- Let's say base image will be a linux image , and let's say in application mentioned above u have dependencies like MySQL and Mongo DB , so this mongo db can also be added as a image in ur container , in short a container is nothing but combination of layers of images combined.
- Similarily all the dependencies will be added as image in our container.

## Difference Between Image and Container
- If we take these layers of images combined all as together then this will be called as Docker Image.
- Once i take up this docker image and probably run this docker image , then internally what will happen is that it will firstly create a container , this container is nothing but its a environment and within this environment considering all the dependencies it will try to run this application.

## Difference Between Docker Image and a Container
- Docker image is a package or artifact and we can move or share this artifact or package in different environments.
- When we run a Docker Image -> it will start the application and inorder to run this application properly what it will do is that it will create a container , install all the dependencies within the container , this container can also be considered as the environment , which will make ensure that all the dependencies will basically be created and then we will be able to run our entire application in this environment.
- Basically docker image when we run it its going to create a container with all the dependencies installed over there , this container is specifically a environment where my application will be running.

- Note : Usually docker images are very small . Why ?? -> Reason coming up

## Docker Vs Virtual Machine
- Docker and Virtual Machine both main task is to perform virtualization , now w.r.t any OS if i install docker how is it going to virtualize my os and if i install virtual machine how is it going to virtualize my os.

## How to Operating System is basically made up of ??
Suppose i take a operating system it can be a linux,windows or mac any of them . If i consider a operating system at base i have a hardware (cpu,ram,etc.) on top of it we have a OS kernel (which is reponsible for all kinds of communication with the hardware) , another layer on the top of os kernal is the application layer(most of the changes w.r.t ui happens in the application layer(for eg. we have different variations of linux like ubuntu , linux red hat so the basic changes between all these linux is that the UI changes the kernel will be almost same)).

- If i consider docker or virtual machine which layer of the operating system will it virtualize ??
- Docker will be virtualizing the application layer of the OS , that basically means docker images will be able to communicate with the os kernel.
- Similarily in the case of VM's they virtualizes both the application layer and the Os kernel layer , whenever we install the VM's at that point of time it will have its own application layer and its own OS kernel layer -> VM is a complete seperate subsystem which is being installed in the host OS. VM will have its own OS kernel
- In docker u have a specific image u pull that image install it and this image will be able to communicate with the OS kernel and this OS kernel is of the host.
- Whereas in VM it has its own OS kernel, whenver u install VM u need to assign some amount of resources from the system like hard disk , RAM seperately to the VM.
- The above is the basic difference between docker and VMs

## Advantages and Disadvantages w.r.t to Docker and VMs
- Docker : Since we are just virtualizing the application layer , docker image size is usually smaller(in megabytes)-> i.e. we can just run the application layer over here and it will communicate with the host OS.
- In case of VM the size will be big because it has its own application layer and its own os kernel layer(in gigabytes).
- Docker Containers start and run much faster when compared to the VMs(why - because it just has a application layer). Application layer it will be communicating with the OS kernel of the host. It is faster because it doesn't have its own os kernel.
- Whereas in case of VM's it has its own application layer and Os kernel, so just to start both of them it will take time -> hence VM is comparatively slower.
- Compatibility : We can install VM on any OS. -> Hence no compatibility issues. But in case of docker images there may be compatibility issues.(Let's say i have a windows machine, in this windows machine i cannot install docker images that are of linux, if i install and try to communicate with the os kernel it might not be possible -> it will be possible if the os kernel supports , i.e. rightnow if u consider windows 10 or greater this supports even dockerlinux images also but windows version < 10 doesn't). Hence compatibility issue has been fixed now after windows 10.
- For installing docker there are system requirements -> go to docker documentation -> the system requirements mentioned under WSL 2 backend. BIOS setting must be enabled open the task manager go to CPU there check for virtualization it must be showing enabled. If not enabled shutdown and restart ur machine and continiously press f11-> by this ur BIOS settings will get enabled.
- Read the Documentation for more details -> Hyper-V and Containers Windows features must be enabled(open windows feature -> there Hyper-V is present and this needs to be enabled)

# Docker Commands
- Commands:
- attach Attach local standard input, output, and error streams to a running container
- commit Create a new image from a container's changes
- cp Copy files/folders between a container and the local filesystem
- create Create a new container
- diff Inspect changes to files or directories on a container's filesystem
- events Get real time events from the server
- export Export a container's filesystem as a tar archive
- history Show the history of an image
- import Import the contents from a tarball to create a filesystem image
- inspect Return low-level information on Docker objects
- kill Kill one or more running containers
- load Load an image from a tar archive or STDIN
- logs Fetch the logs of a container
- pause Pause all processes within one or more containers
- port List port mappings or a specific mapping for the container
- rename Rename a container
- restart Restart one or more containers
- rm Remove one or more containers
- rmi Remove one or more images
- save Save one or more images to a tar archive (streamed to STDOUT by default)
- start Start one or more stopped containers
- stats Display a live stream of container(s) resource usage statistics
- stop Stop one or more running containers
- tag Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
- top Display the running processes of a container
- unpause Unpause all processes within one or more containers
- update Update configuration of one or more containers
- wait Block until one or more containers stop, then print their exit codes
- docker -v -> To know the current version
- U can search many public images that are present inside docker from the docker hub.

## Running a Sample Container
- docker run -d -p 80:80 docker/getting-started -> if we write this command in command prompt then 'getting-started' -> this image will basically get pulled from the docker hub and then it will run as a container within my machine. 'getting-started' is a public image which is available in the docker hub u will get it if u search it up.

- Docker pull command : docker pull docker/getting-started -> to use/pull this image from the docker hub repository u have to use this command.

- There in this public image if u go to the Tags section u will be able to see the recent tags that are updated in this specific docker image. Different tags w.r.t different images that are present in the docker hub.

- To download this image(getting-started) write command: docker pull docker/getting-started in the command prompt. When u download the image it does not come as a container directly , it becomes container when we run it , to run that image we have to use a seperate command.

- When u write this command in ur command prompt : docker pull docker/getting-started -> ur docker image will get downloaded and ur default tag will be : latest.(Pulling this image from docker hub repository) U will see that a lot of layers have been pulled as this docker image is downloaded(as this docker image will be having multiple layers with dependencies converted in form of image)-> all those layers will get downloaded these are like smaller images

- Use command docker images -> it will give the list of all the images downloaded (to check whether ur image is downloaded or not).

- Go to Docker Desktop : There in images u will see that this getting-started image has got installed. -> it is keeping track of all the images that are getting downloaded.

- Run the image : docker run -d -p 80:80 docker/getting-started -> when u run this image u will also be able to access it from my local machine.

- docker run: For running the docker image, -d : this will run the image as a container in a detached mode i.e. independently it will be running. -p : assigning port and mapping port from our localhost(ur host machine where u are working, where u are running the container , ur container environment and host environment will be different), 80:80 means that i m assigning my host port as 80 , from host port i will communicate with my container port and that container port will also be 80.

## Container Port and Host Port
- Let's say i have downloaded the docker image , as soon as i run this docker image -> this will create an environment(container environment), and this container environment is actually running in my host(in my windows machine(application is running there)).
- Inorder to access this application from my host machine(windows) i have to access it from some port for local machine here its 80 i.e. 127.0.0.1:80(80 port for host), also to access the application from the container we require a port here we assign it to 80 . i.e this port is opened from this container environment. So this mapping is basically done from the above command. 80:80 -> first 80 means host environment port(windows) , second 80 means we are trying to access the container application which is there in container(exposed from the container.)
- "getting-started" is the name of the image and 80:80 basically means assigning host port to the application port.
- docker ps -> to verify whether the container is working or not (to check whether the docker is running as a container)
- On url do : 127.0.0.1:80 and then press enter -> u will see that getting started application has started.

## Basically:
- -d : run the container indetached mode(in the background).
- -p 80:80 : map port 80 of host to the port 80 in the container
- docker/getting-started : the image to use
- docker ps : a command to check whether the docker is running or not
- When u do : docker ps -> u get whether the docker is running or not (i.e. container is running or not) , in the outputs u get after using docker container we have something called as container id.
- To stop the container : docker stop "container id pasted" press enter , then if u do docker ps there u will see no container is running now(i.e the docker container has stopped)
- if u do docker image -> there u will see that the image is their.
- docker run -d -p 80:80 docker/getting-started u execute this again , then when u go to docker desktop u will see that the container run history is getting showed.(in previous history when did we started and exited that information is also there)-> whatever docker images u runned as a container that all information is available over here. U can delete , resume , restart the ontainers from the containers section in the docker desktop
- docker ps -> to get the container id
- docker stop "container id"
- command : docker images -> u will get the image id of all the available images
- then use : docker image rm "image id" -> this will remove the image.
- if the above commands throws a error then we remove it forcefully : docker image rm -f "image_id"
- then use docker images -> that image(whose id was passed) has got deleted.

## Trying Hello World Docker Image
- Search hello world image on docker hub
- Pull the image: (Commands are given when u search hello world image in the docker hub)
- docker pull hello-world
- docker run hello-world(u can directly run this also if the image is not present it will pull the image from the repository)
- To try something more ambitious, you can run an Ubuntu container with:
- docker run -it ubuntu bash
- docker images hello-world
- If u do docker ps after running the hello world docker image u will not find any container because this docker image will just display the content and then it will get exited.
- if u do docker images -> then this hello world image will be available.

## Image Redis
- Search on docker hub -> We will get redis -> pull it by docker pull redis -> w.r.t this we also have a lot of tags by default it pulls latest tag(we can specify tag also : docker pull redis:latest) -> latest tag means latest version will get downloaded.
- There are multiple tags , suppose if u want a tag like bullseye u can use that also : docker pull redis:bullseye(different tags -> different versions of container we will be able to run)

## Note:
- We can run any number of containers on the same port , let's say we have a container for hello world we can create another container for getting started and these both can be assigned to the same port.
- Container port can be same for both the images "Hello World" and "getting-started". For both of these images container port can be 80.
- But host port should always be different(for both the images) -> two images cannot have same host port but they can have same container port.(For eg. if host port 5000 and container port 80 -> 5000 will be linked to 80)
- Port is not necessarily 80:80 it can be any number.
- Host port can be configured based on ur host environment whichever port is available with that(80,500,10 etc.).
- Docker Hub Repository : Where u can push docker images(created by u). -> any person will be able to download it(image) and run it as a container.