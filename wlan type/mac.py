#!/usr/bin/python3
import os
import subprocess

def macchanger(opt):
    subprocess.call(["sudo","service","NetworkManager","stop"])
    subprocess.call(["sudo", "ifconfig", opt, "down" ])
    subprocess.call(["sudo","macchanger","-r",opt])
    subprocess.call(["sudo", "ifconfig", opt, "up" ])
    subprocess.call(["sudo","service","NetworkManager","start"])
def macchangerman(opt):
    subprocess.call(["sudo","service","NetworkManager","stop"])
    subprocess.call(["sudo", "ifconfig", opt, "down" ])
    subprocess.call(["sudo","macchanger","-m", mac, opt])
    subprocess.call(["sudo", "ifconfig", opt, "up" ])
    subprocess.call(["sudo","service","NetworkManager","start"])

print("MAChanger by stosempreingiro")
os.system('sleep 2')
os.system('clear -x')

print("Wifi interfaces:")
"""
"""
k=os.popen("ifgrp").read()
j=k[:6]
s=k[8:14]
t=k[16:24]
print("[1]",j)
if s:
    print("[2]",s)
if t:
    print("[3]",t)
"""
"""
i = input(("Choose [1/2/..]: "))
"""
"""
scegli=input(("Change MAC manually? [y/n]: "))
if scegli == "y":
    mac=input(("Write MAC here [XX:XX:XX:XX:XX:XX]: "))
    if i == str(1):
        macchangerman(j)
    elif i == str(2):
        macchangerman(s)
    elif i == str(3):
        macchangerman(t)
    else:
        print("[!] Error")
elif scegli == "n":
    if i == str(1):
        macchanger(j)
    elif i == str(2):
        macchanger(s)
    elif i == str(3):
        macchanger(t)
    else:
        print("[!] Error")
else:
    print("[!] Error. You can only choose y/n")
