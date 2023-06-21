#!/bin/bash

echo ""
echo "#########################"
echo "Installing docker..."
echo "#########################"
echo ""

sudo apt-get install -y \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common

curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -

sudo add-apt-repository  -y \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable"

sudo apt-get install -y docker-ce docker-compose-plugin

if id -nG "$USER" | grep -qw "docker"; then
    echo ""
else
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
fi

sudo chmod 666 /var/run/docker.sock

if ! command -v docker &> /dev/null
then
    echo "Setup failed!"
    echo "Failed to install docker!"
    exit 1
fi

echo ""
echo "#########################"
echo "docker installed"
echo "#########################"
echo ""

