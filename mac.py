#!/usr/bin/python3
import subprocess
import netifaces

def macchanger(interfaccia):
    subprocess.call(["sudo", "service","NetworkManager","stop"])
    subprocess.call(["sudo","ifconfig",interfaccia,"down"])
    subprocess.call(["sudo","macchanger","-r",interfaccia])
    subprocess.call(["sudo","ifconfig",interfaccia,"up"])
    subprocess.call(["sudo", "service","NetworkManager","start"])

interfacce=netifaces.interfaces()
i,j=1,0
for interfaccia in interfacce:
    if interfaccia=="lo":continue
    print(str(i)+")",interfaccia)
    i+=1
try:
    user=input("Scegli interfaccia: ")
    if user=="exit":
        exit()
    else:
        user=int(user)
    while j<=len(interfacce):
            if user<=len(interfacce)-1:
                j+=1
                if user==len(interfacce)-(len(interfacce)-j):
                    macchanger(interfacce[j])
                    break
            else:
                print("[!] mmh.. non conosco questa interfaccia")
                break
except ValueError:
    print("[!] mmh.. qualcosa è andato storto.. riprova.")
