#! /bin/bash

echo -e "\e[1;33m* installing pip modules...\e[0m"
pip3 install -r requirements.txt
echo -e "\e[1;33m* copying executable...\e[0m"
sudo cp xkcd.py /bin/xkcd
echo -e "\e[1;33m* \e[42mfinished!\e[0m"
