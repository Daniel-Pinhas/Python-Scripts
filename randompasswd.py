#!/usr/bin/python3
import random 
import string
import sys

lvlpwd = input("Enter the level of the wanted password: Strong , Medium, light: ")

while lvlpwd not in ["strong", "medium", "light"]: 
    print("Wrong please enter wich password lvl you would like..")
    lvlpwd = input("Enter the level of the wanted password: Strong , Medium, light: ")   

passwd = []

if lvlpwd == "strong":
    while len(passwd) != random.randint(12,16):
        passwd.append(str(random.randint(0,9)))
        passwd.append(random.choice(string.ascii_letters))
    print("".join(passwd))
    sys.exit(1)    
        
if lvlpwd == "medium":
    while len(passwd) != 10:
        passwd.append(random.choice(string.ascii_letters))
        passwd.append(random.choice(string.ascii_letters)) 
        while len(passwd) != 10:
            passwd.append(str(random.randint(0,9)))
        print("".join(passwd))
        sys.exit(1)  

if lvlpwd == "light":
    while len(passwd) != 8:
        passwd.append(str(random.randint(0,9)))
    print("".join(passwd))
    sys.exit(1)      


