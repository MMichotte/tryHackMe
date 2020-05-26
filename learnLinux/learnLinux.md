# Notes for [Learn Minux](https://tryhackme.com/room/zthlinux) room 

## Usefull commands :
```bash
# List all files with detailed information on permissions and ownership
ls -la  

# Change user
su {username} 

# Redirect output to file
> #example: echo hello > file.txt

# Append to end of file 
>> 

# Run command in background
& #example: sleep 5 &

# Change file permissions
chmod xxx file # xxx -> see permissions below

# Find something somewhere 
find # See man page! 
#examples : 
# find files and dirs that contain a.txt in their name
find / -name a.txt 
# find all files (-type f) on this computer (/) belonging to a user (-user <insert-username-here>) and redirect error output to null (2>>/dev/null)

find / -user <insert-username-here> -type f 2>>/dev/null

# execute as superuser:
sudo 

# execute as specified user:
sudo -u <user>

# show curent user sudo permissions:
sudo -l 
```

#### File Permissions:
Number | Permission Type | Symbol
-------|-----------------|-------
0      | No Permission	 | ---
1	   | Execute	     | --x
2      | Write	         | -w-
3	   | Execute + Write | -wx
4	   | Read	         | r--
5	   | Read + Execute	 | r-x
6	   | Read +Write	 | rw-
7	   | Read + Write +Execute | rwx

#### Output redirection :
```bash
 > file #redirects stdout to file
1> file #redirects stdout to file
2> file #redirects stderr to file
&> file #redirects stdout and stderr to file
```