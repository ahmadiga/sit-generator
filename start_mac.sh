#!/usr/bin/env bash
#sudo apt-get update
sudo brow python git npm -y
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
