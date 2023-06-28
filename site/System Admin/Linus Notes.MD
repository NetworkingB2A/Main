# Basic notes
### Wildcards
Wildcards|meaning
-|-
*|Matches any characters
?|Matches any single characters
[<i>characters</i>]| Match any character that is a member of the set <i>characters</i>
[<i>!characters</i>]| Match any character that is a not member of the set <i>characters</i>
[[class]]|Match any character that is a member of the specified class 

Class|Meaning
-|-
[:alnum]|Matches any alphanumeric character
[:alpha]|Matches any alphabetic character
[:digit]|Matches any numeral
[:lower]|Matches any lowercase letter
[:upper]|Matches any uppercase letter

## Linux file notes

Directory|Purpose
-|-
/|root directory
/bin|Contains binaries(programs) that must be present for system startup
/boot|Contains linux kernel. initializes RAM disk image and boot loader
/dev|Special directory that contain device nodes. "Everything is a file in linux. Here is where the kernel maintains a list of all the devices it understands
/etc|This directory contains all the system-wide configuration files. 
/home|Each user is given a directory in /home. It is like the user folder in windows
/lib| Contains shared library files used by the core system programs.like DLLs in windows
/lost + found|It is used in the case of a partial recovery from a file system corruption event. Unless something bad happens this folder will remain empty
/media|On modern linux systems, this directory will contain the mount points for removable media such as USB drives. 
/mnt|On older linux systems this directory contains the mount points for devices that have been mounted manually.
/opt|Used to install "optional" software. Mainly used to hold commercial software products
/proc|This directory is special. It's not a real file system in the sense of files stored on your hard drive. It's a virtual file system maintained by the kernel. The files contain peepholes into the kernel itself
/root|Home directory for the root user
/sbin|System Binaries. Needed for the system to run. Accessed only by a super user.
/tmp|used for temp storage of devices
/usr|It contains all program and support files used by a regular user.
/var|This directory is used often and hold data about the system.
/var/log| This is where system logs are stored.


## Basic linux commands
Command|Name|Description|Extra vars
-|-|-|-
pwd|Present working directory|Shows the directory that you are currently in
cd {path name}|Change directory| change to a different directory
ls {path name or argument}| List directory contents|
less|opposite of more| allows you to scroll up and down in a test file (useful)
mv|
cp|
mkdir||| -p (adds recursive directories)
ln original-file-or-directory new-link|link|Creates a link Hard be default|-s (used to create a symbolic link)
rm|||-r (means recursive), -f (means force), -rf (recursive and force)

## Tech support commands
Command|Name|Description|Extra vars
-|-|-|-
systemctl {start|stop|reboot|ect} (service)
hostnamectl|
which (application name)|
apt show (application name)
ps|ps| used to see the top running processes| -ef(to see top processes)
whoami
ip link|ip link|tells some data about a link
ip addr | ip address| This will tell you your ip address

## tcpdump
tcpdump is a tool that allows you to sniff traffic from a devices interfaces.
example of command below
tcpdump -i {interface name} -v src {source ip} and dst {destination ip}

tcpdump flag types
|Flag| What it does|
|-|-|
|host| Specify the any traffic to or from a ipaddress or DNS name.|
|net| Network to watch |
|-v| verbose mode| 
|-w {filename.pcap}| write out a file| 


|capture filter| What it does|
|-|-|
|and, or, not| if combining filters you must use these commands.|
|src| Specify any traffic sourced from an IP address or DNS name.|
|dst| Specify any traffic destined  from an IP address or DNS name.|
|tcp| tcp protocol capture|
|udp| udp protocol capture|
|port| This is to watch traffic that is using a range of ports or a individual port. |

## Wget
Wget will allow us to download files from the internet to the server.

Example below
wget {download url}
|Flags | What the flag does|
|-|-|
| -O {filename} | This will allow you to change the name of the file.|
| -P {custom path}| This will allow you to change the location where the file will download to.|
| -c | This will allow continue a download that interrupted for some reason.|
| -i | This will allow you to use an input file. incase you wanted to download a bunch of files at once that you call out in a file.|

## cURL
Curl will allow you to do a api call to web server.

curl url

## link types

Symbolic links
- This is really like a shortcut on windows
- It is a pointer to the file
- If you delete the original file, the symbolic link will become useless
- This is the more modern way of creating links
- Different iNode numbers
Hard links
- A different name for the same file
- same file size
- Same iNode numbers
- Deleting the original file, will still allow hard links to be operational
Here is a picture of the two links  
![Picture of two link types](../images/symVShardLinks.png)

What is a Daemon?
- A type of program on unix-like operating systems that run unobtrusively in the background. 
- sshd is a good example. sshd is a program hat is always running, ready to accept or send ssh connections.

## Notes
log files are stored under /var/log
- if you want to learn about less, more, grep, ect. log files are good for learning about the basics