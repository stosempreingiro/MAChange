#!/bin/bash
sudo apt install macchanger -y
sudo apt install net-tools -y
sudo cp ifgrp.sh /usr/local/bin/ifgrp && sudo chmod +x /usr/local/bin/ifgrp
sudo cp mac.py /usr/local/bin/mac && sudo chmod +x /usr/local/bin/mac
clear -x
sleep 1
echo "Write 'sudo mac' on your terminal to start macchanger ;)"
sleep 1
