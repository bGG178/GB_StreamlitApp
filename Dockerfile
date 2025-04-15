#base image
FROM python:3.12-slim

#workdirectory location (not 100% sure what this does entirely, i know it sets the default location for command execution)
WORKDIR /streamlit_app/main

#copy app's files
COPY . /streamlit_app/main

#install requirements with pip from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#open the web port to access Streamlit with
EXPOSE 8501

#run
CMD ["streamlit", "run", "main/app.py", "--server.port=8501", "--server.address=0.0.0.0"]


#Putting this here because it was a really helpful comment someone left on reddit explaining what Docker's purpose is
#I struggled with understanding it during lecture, so this explanation helped

#Imagine writing a Hello, World program in, say, Node.js. So, you'd write maybe this in a main.js file:

#console.log("Hello, world!");

#And to run it, assuming Node.js is installed, you just do:

#node main.js

#So, how do you distribute that to people? Well, easy enough, it's just one .js file, right? You can just email it to them! Ok, great, now they have the code, but what if they happen to have a really old version of Node installed that doesn't support console.log()? (that doesn't actually exist, that was there from day one, but let's pretend for a moment that it was added in Node v5, for example, so anyone with Node v1-v4 won't be able to run that program). When they go to run the program, it won't work.

#Docker is a solution to this problem.

#Pretend that you zip'd up the directory that source file was in. So, it's just maybe /home/usera/main.js in the .zip archive. What if there was a way to include the version of Node you have installed, the one you know the program works with? Well, you might consider moving your node installation directory into /home/usera too, then zip the directory up. Now you can send that archive to someone, and they can run your program using THAT version of Node and you'd be guaranteed it would work.

#That's essentially what Docker does. There is, of course, a bit more to it than that, but in simplest terms, that's what it is.

#To go into more detail... docker works not with archives, but with images. An image is... well, in a lot of ways it IS an archive! But it's an archive that you build by adding layers to it. Most of the time, you start with a base layer that already exists, and more times than not it'll be one based on an operating system. Meaning, conceptually, you can imagine zipping up your ENTIRE hard drive, so now all the operating system files are included too. That's in effect what a Docker image is.

#Then, on top of that layer, you add any things your application depends on. In the case of our little Hello World app, which means Node. But rather than just copying it somewhere and adding it to the image, you instead specify the commands you would normally use to install Node. You in a sense pretend you're installing your OS from scratch, then all the things your app needs to run, then finally your app iself. You might install node by doing:

#sudo apt install nodejs

#And indeed, as you're building your image, that's exactly what you would specify. You would then say "Hey, Docker, go build this image for me using these instructions", which would include that command. Docker will get the base Linux image, then effectively execute that command, installing Node into that image. That becomes a layer ON TOP of the base layer in your image. You might wind up with Node installed in /usr on the file system in the image.

#Then, the next instruction Docker will execute (which, along with the Node install instruction, is specified in a Dockerfile usually, or a docker-compose file if you prefer, but either is just instructions telling Docker what to do to build your image) might be to copy the main.js file into the image. At the end, you have an image that includes Node and your application. Finally, the last instruction you tell Docker about is the command to execute when the image is started (well, when a container is created from the image to be precise). In this case, it's the same command you use to run the program on your machine.

#Now, you can distribute that image to people, and you now know with complete certainty that they will be able to run your app because everything they need - right down to the OS - is there in the image. Think about what this means for a minute... it's not just what's installed, it's how the environment is set up. What if your program depends on environment variables? You can run commands when the image is built to set them. What if there are memory settings or something that have to be tweaked for it to run? You can include those commands, as if you executed them yourself, and Docker will execute them when the image is built. There's no guesswork, as long as you specify all the commands needed accurately then it will Just Work(tm). The final image you can think of as a snapshot of what the machine you built up with all those commands was at the end. That's what it will be when someone spins up a container from that image (or multiple containers - because you can absolutely do that since all containers are isolated from each other... more on this next!).

#While it doesn't matter TOO much when you're actually using Docker, you should know that while CONCEPTUALLY you can view containers, for the most part, as you would a VM, a container is definitely NOT a VM.

#A VM is a complete hardware machine, and the software installed on it, emulated by the host machine it's running on (well, to be pedantic, that's true of SOME types of VMs, but not necessarily all... but for our purposes here that doesn't much matter). Containers, on the other hand, actually share the resources of the machine they're running on, but they are isolated from the physical machine, and from each other. Instead of with a VM where you might have a whole Linux kernel in the VM running on top of the kernel of the host machine, with a container the kernel of the host machine is actually being called directly by the code in the container. It's being shared by the container and the host machine's OS. While it doesn't make a difference from the point of view of your application code inside the container, it makes a difference generally because this is the reason containers can start up so fast and why you can have many containers running on one physical machine, typically many more than you could have VMs. VMs use a lot of memory and CPU time since they are emulating the hardware AND software of a virtual machine (hence the name!), but containers functionally act just like other programs running on one machine. They use much less resources and are much faster (again, you can always find exceptions, so this is a general statement only).

#so, we benefit from containers primarily by (a) ensuring the runtime environment is EXACTLY what we need it to be without any doubt, and (b) they are much more lightweight in terms of resources and much faster than VMs.

#It's not a virtual machine. Docker does not run any kernel. It does not interface with the devices like a kernel would. It's not an operating system. What it is, is just a collection of binaries that can run on an existing Linux kernel. Aside from the binary that you need (your compiled program, or the target interpreter), it contains the full dependency tree of libraries all the way to glibc or musl or whatnot. It makes sure that everything that the program needs, exists and is available exactly like the application wants.
#https://www.reddit.com/r/AskProgramming/comments/15ctngm/what_exactly_is_docker_and_how_do_i_benefit_from/
