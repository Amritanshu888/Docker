## flask app for hello world

from flask import Flask
import os
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000) ## host = 0.0.0.0 can access ur local address also and ur host address also
    ## Command prompt me jake do : ipconfig -> u will be able to see ur local ip address , local host address and many more things.
    ## IPV4 -> me available hai(this is ur local ip address) -> run it on browser by giving 5000 as a port id_address:5000
    ## u will see ur web page there. U can run this from localhost also it will give u the same thing

## Now creating a Docker Image 
## -> To create a docker image u will first create a file named : Dockerfile
# -> In Dockerfile we will write certain commands and these commands will help us create a docker image.
## Note: The lower base image should be a linux kernel or linux os.
# One of the linux image from the docker hub repository: python:3.8-alpine , can also use -> python:3.7-alpine(this is the base image).
## Why we use python:3.8-alpine ---> why we use this is bcoz it will be very small in size and can be quickly created as a base and run it as a container.
# The command will try to pull this base image from the docker hub repository. FROM python:3.8-alpine
## COPY Command : From my local repository that is my current working location the both the files(whatever files u have) should be put up inside my base image
# in one folder , let's say this folder is app -> in short in my docker image i m creating a app folder and all the files present over here (in my repo(currently where im working))
# will be copied inside my app folder. This app folder will be created in the container/docker image
# Command: COPY . /app -> . says my local repository
## After this we setup my working directory : Since copying all the files in the app folder so my working directory should be the app folder.
# Command : WORKDIR /app
## Then to install all the dependencies we have it in out folder requirements.txt so we use : RUN pip install -r requirements.txt
## Then CMD python app.py -> the command that we are going to run. If we do this whatever files will be present in ur 
## app folder which we have created in our container will be executed(first it will install libraries from requirements.txt and 
## then it will execute the app.py file)
## From the docker file a docker image will get created(which will contain or the files in ur current directory)



## Commands for building the image
## docker build -t welcome-app . -----> here "welcome-app" is the docker image name which we are giving here. This the command for building the 
## docker image
## Command : docker images ---> To see whether docker image is built or not.

## Running the docker image as a container
## When u run a docker image two important info to be given is ur host port and ur container port(that mapping needs to happen)
## We will not be running this in a detached mode so no -d , also lets keep host port as 5000 and container port as 5000.
## docker run -p 5000:5000 welcome-app -> command to run the created docker image
## When u run this u will be able to see two IP : One of host port and other of container port.
## This application is running inside my container, with the help of port from my localhost/local ip address , from my localhost port
## i m accessing the application which is present inside my container.
## Container port -> won't show anything , while localhost port will display the application when u hit the url.(U can't directly access the ip of the container).
## U can access it from the localhost port id only.
## To see whether ur container is running or not :
## Use docker ps -> This will show which all containers are running.
## Container port is : 0.0.0.0:5000 (will get to see after executing docker ps)
## To stop the container from running : docker stop "container_id" ---> container_id will be available when u run docker ps -> to see the running container.
## When we push/pull the image to docker hub repository u will be able to pull it , run it and access it on the same localhost port id 0.0.0.0:5000


## The deployed repo should be a public repo , u should be able to access it and run in ur own localhost machine.
## Step 1: Login to docker hub  (from ur desktop)
## Commands : docker login
## docker images  -> u will get to see the images welcome-app
## U have to rename this image
## 2 ways to rename
## Way 1 : Remove it and rebuild it
## docker image rm -f welcome-app
## Then execute docker images ---> No image is present
## Now we have to build it , note that it is better that u also give ur username , format : docker build -t username/image-name .
## command : docker build -t username/welcome-app .  ---> this is how rename has to happen
## docker images ----> u will be able to see renamed images
## Way 2 : Directly use docker tag and change the name of the image also.
## Eg. command : docker tag username/welcome-app username/welcome-app1
## docker images -> another image will be created with this image name.
## Note : If u want to push ur image to docker hub repository u really have to use ur username : username/image-name
## Pushing the image : docker push username/welcome-app:latest ----> latest will basially show the tag over their
## If any new updates are coming we can create the same docker image with a different version --> this is useful for making sure ur
## docker image keeps on updating
## docker push username/welcome-app:latest  ---> Command to push image to docker hub.
## On the docker desktop ur pushed image will be available , u can visit that in tags section u will see the command to pull ur created
## docker image , docker pull username/welcome-app --> then run it in ur own local machine
## docker image rm -f username/welcome-app:latest  --> remove the image
## docker images ----> to see the existing images
## docker pull username/welcome-app:latest   ---> pulling ur image
## docker images ---> image will be available there
## docker run -d -p 5000:5000 username/welcome-app:latest ---> mapping 5000 of host to 5000 of the container port.(This time running in detached mode).
## Then on ur localhost with port 5000 u will be able to see it running.
