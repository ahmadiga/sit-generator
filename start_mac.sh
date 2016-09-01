#!/usr/bin/env bash
#sudo apt-get update
brew install python python git npm -y
pip install --upgrade pip
pip install virtualenv
npm install npm -g
npm install -g bower
gem update --system
gem install compass
wget https://raw.githubusercontent.com/ahmadiga/sit-generator/master/start.py
python start.py
rm start.py
rm start_mac.sh
echo "Thank me welak"

