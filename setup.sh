#!/usr/bin/bash

echo -e "\nInstalling system packages...\n"
sudo apt update
sudo apt install python3-tk

echo -e "\nSetting up Python virtual environment, This can take a while...\n"
python3 -m venv venv
source venv/bin/activate

echo -e "\nInstalling Python dependencies in virtual environment...\n"
pip install -r requirements.txt
