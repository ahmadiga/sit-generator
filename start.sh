#!/usr/bin/env bash
#sudo apt-get update
sudo apt-get install software-properties-common python python-dev python-pip git -y
sudo pip install --upgrade pip
sudo pip install virtualenv
wget https://raw.githubusercontent.com/ahmadiga/sit-generator/master/start.py
python start.py