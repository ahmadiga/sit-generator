#!/usr/bin/env bash
#sudo apt-get update
sudo apt-get install software-properties-common python python-dev python-pip git npm ruby-dev rubygems -y
sudo pip install --upgrade pip
sudo pip install virtualenv
sudo npm install npm -g
sudo npm install -g bower
sudo gem update --system
sudo gem install compass
wget https://raw.githubusercontent.com/ahmadiga/sit-generator/master/start.py
python start.py
rm start.py
rm start.sh
echo "Thank me welak"
