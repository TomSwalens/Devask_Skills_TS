Task name:
Docker
Task preparation:
VM with linux OS.
Task implementation:

How to do this task can be seen in the apachetoms.sh script.

In there you can see how the system updates and installs the req dependencies. Clones the index + js from my github. Makes the dockerfile. Builds the image. And launches a container on port 8088.
Finished with a small sleep + curl for verification.

Task troubleshooting:
Change of the url for the git clone in the bash script.
Making the .sh script executable with chmod +x *.sh



Task verification:
Screenshot under Docker
https://docs.google.com/document/d/1sJQKWfi7IL6FfIjJBT3c5zstpOfB3hE3WigJU2X5QX4/edit?usp=sharing
##########################################################################################################
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3 is already the newest version (3.8.2-0ubuntu2).
0 upgraded, 0 newly installed, 0 to remove and 618 not upgraded.
sudo: pip: command not found
Cloning into 'Docker'...
fatal: repository 'https://github.com/TomSwalens/Devask_Skills_TS/tree/main/Docker/' not found
apachetoms.sh: 7: cd: can't cd to Docker
Building docker File...
Dockerfile made.
Using default tag: latest
latest: Pulling from library/httpd
Digest: sha256:7765977cf2063fec486b63ddea574faf8fbed285f2b17020fa7ef70a4926cdec
Status: Image is up to date for httpd:latest
docker.io/library/httpd:latest
Sending build context to Docker daemon  6.144kB
Step 1/3 : FROM httpd:2.4
 ---> 1132a4fc88fa
Step 2/3 : COPY files/index.html /usr/local/apache2/htdocs/
 ---> Using cache
 ---> 7323e62a3827
Step 3/3 : COPY files/script.js /usr/local/apache2/htdocs/
 ---> Using cache
 ---> eacea23c4d15
Successfully built eacea23c4d15
Successfully tagged dockerimagetomswalens:latest
docker: Error response from daemon: Conflict. The container name "/containertomswalens" is already in use by container "b0a57791334079262d6b48993979734faf99dd45ab998ff96139ad679b786e38". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
<html>
<head>
    <title>DevNet Associate Skills Test: Tom Swalens</title>
</head>
<header> DevNet Associate Skills Test </header>
<body>
    <h1>Created by Tom Swalens</h1>
    <h1 id="datetime"></h1>

    <script src="script.js"></script>
</body>
</body>
</html>