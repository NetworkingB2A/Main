There are multiple container types. these include
- LXC
- LXD
- LXCFS
- and more

Docker uses LXC containers. 

keep in mind the following an OS is comprised of two things the OS kernel and software. The kernel is was interacts with the hardware. software is what interacts with the kernel drivers, user interfaces, gui, ect.
Containers share the underlying kernel. You are not able to run a windows docker container inside a linux kernel. 

Docker does not have as much isolation between docker containers, VMs on the other hand do have true isolation from each VM.

