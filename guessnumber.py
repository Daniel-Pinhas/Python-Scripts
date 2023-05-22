#!/usr/bin/python3
import time
import random
import sys 

print("Think about 1 or 2 Digits Number and I Would Guess It..")

time.sleep(3)
x = 0
l = 0
h = 99

 

while x != "correct":
    num = str(random.randint(l,h))
    print(("I Guess ") + num )
    while x != "correct":
        x = input("Correct? Higher? Or Lower? ")
        if x not in ["correct", "higher", "lower",]:
            print("Valid insert please type correct, higher or lower")
            x
        if x == "higher":
            l = int(num) + 1
            num = str(random.randint(l,h))
            if h == l :
                print("Got It! " + num)
                sys.exit(1)
            print(("I Guess ") + num )
        elif x == "lower":
            h = int(num) - 1
            num = str(random.randint(l,h))
            if h == l:
                print("Got It! " + num)
                sys.exit(1)
            print(("I Guess ") + num )
    print("Got It!")
    

