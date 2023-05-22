#!/usr/bin/python3
"""""
x= input("Enter a number ")

y = (int(x))
z = y%2

if z == 0:
    print("The number is even")
else:
    print("The number is odd")

if y%4 == 0: 
    print("The number can be devides by 4")
"""

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number"))

if num1%num2 == 0:
    print("The first number can be devides by the second ")
else:
    print("The first number cannot devides by the second ")
