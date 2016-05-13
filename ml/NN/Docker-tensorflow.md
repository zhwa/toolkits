#### Install Gooogle Tensorflow on 64-bit Windows

 - Install Docker Windows Toolbox
 - Open a Windows cmd window and run the following commands:
 	
		 docker-machine create vdocker -d virtualbox
		 FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd vdocker') DO %i
		 docker run -it -p 8888:8888 b.gcr.io/tensorflow/tensorflow


#### Run Docker based Tensorflow

- Open Docker Quick Start terminal. This will automatically start the Virtualbox default machine in the backend.

- Check Virtualbox VM, start your tensorflow VM ("headless start").

- Open a Windows cmd window and run the following commands:

		 FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd vdocker') DO %i
		 docker run -it -p 8888:8888 b.gcr.io/tensorflow/tensorflow

- Visit [http://192.168.99.101:8888/](http://192.168.99.101:8888/)


Since Docker usually needs to have the same operating system on the Docker host system as it's in the Docker container (well, parts that is) you need a Linux VM to run a Docker container that is based on Linux under Windows. Docker itself opens port 8888 between the VM and the container. You have to explicitly tell it to forward the port from the outside of the VM to the open Docker container port by using said parameter -p 8888:8888.


#### Some useful resources

 - Stanford CS224d: [2016 CS224D Lecture Videos](https://www.youtube.com/playlist?list=PLmImxx8Char9Ig0ZHSyTqGsdhb9weEGam)
 - [Tensorflow Tutorials using Jupyter Notebook](https://github.com/sjchoi86/Tensorflow-101) 

