#!/bin/bash
cd '/home/pi/simple-gpio-api'

#Install python 3
printf "\n_____________________________\n Update packages (1/5)\n_____________________________\n"
sudo apt-get update
printf "\n_____________________________\n Install python 3 (2/5)\n_____________________________\n"
sudo apt-get install python3


#install pip3
printf "\n_____________________________\n Install python 3 pip (3/5)\n_____________________________\n"
sudo apt-get install python3-pip

#Install swagger requirements
printf "\n_____________________________\n Install swagger requirements (4/5)\n_____________________________\n"
sudo pip3 install -r requirements.txt

sudo chmod u+x ./start.sh

printf "\n_____________________________\n Installation done (5/5)\n_____________________________\n"