#!/usr/bin/python3
import sys

def func():
    choice = "Wrong"

    while choice.isdigit()==False :
        choice = input("Enter how many Fibonnaci numbers to generate! ")

        if choice.isdigit()==False:
            print("Wrongly entered: ")
        else:
            return int(choice)

x = func()
n1, n2 = 0, 1
count = 0

while count < x:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1


















