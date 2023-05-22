#!/usr/bin/python3
import sys

x = (input("Enter 2 Digits number: "))
if int(x) > 99:
    print("Too Much Digits")
    x = (input("Enter 2 Digits number: "))
    
lst = [1, 2 ,3 ,4 ,5 ,6 ,77 ,8 , 9]

while True:
    if int(x) in lst :
        print("Your number is in the list!")
        sys.exit(1)
    else: 
        print("Your number is not in the list!")
        x = (input("Enter 2 Digits number: "))
        if int(x) > 99:
            print("Too Much Digits")
        x = (input("Enter 2 Digits number: "))

    













