#!/usr/bin/python3

import sys
import random as rnd

num = input("Enter a number between 1-9 ")

if int(num) in [1,2,3,4,5,6,7,8,9]:
    pass
else:
    print("Type only numbers between 1 - 9")
    sys.exit(1)

while True:
    for i in range(1):
        rnd_num = rnd.randint(1, 10)
        x = rnd_num
        if int(x) == int(num):
            print("Youre Right!")
            sys.exit(1)
        elif int(x) > int(num):
            print("Youre Too Low!")
        elif int(x) < int(num):
            print("Youre Too High!") 
        num = input("Enter a number between 1-9 ")
