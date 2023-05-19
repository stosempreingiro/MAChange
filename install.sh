#!/bin/bash
sudo apt update
echo "INSTALLING MACCHANGER"
sudo apt install macchanger -y
sudo apt install python3
sudo apt install python3-pip
python3 -m pip install netifaces
sudo apt install python3-netifaces
sudo mv mac.py /usr/local/bin/mac
sudo chmod +x /usr/local/bin/mac
clear -x
echo "INSTALLAZIONE RIUSITA"
echo "[IT] Scrivi 'sudo mac' nel tuo terminale per cominciare"
echo "[EN] Installatione complete. Write 'sudo mac' on your terminal."
sleep 0.7
echo "Source code: https://github.com/stosempreingiro/MAChange"
echo "-stosempreingiro"