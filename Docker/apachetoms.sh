#!/bin/bashS
sudo apt-get install python3
sudo pip install git

git clone https://github.com/TomSwalens/Devask_Skills_TS

cd Docker
### make docker file
echo "Building docker File..."
rm Dockerfile
touch Dockerfile
echo "FROM httpd:2.4" >> Dockerfile
echo "COPY files/index.html /usr/local/apache2/htdocs/" >> Dockerfile
echo "COPY files/script.js /usr/local/apache2/htdocs/" >> Dockerfile
### build + run container 
echo "Dockerfile made."
docker pull httpd
docker build -t dockerimagetomswalens .
docker run -dit --name containertomswalens -p 8088:80 dockerimagetomswalens

### sleep for 5 sec and verify 
sleep 5
curl localhost:8088