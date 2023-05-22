#!/usr/bin/python3
import sys

def func():
    choice = "Wrong"
    
    while choice.isdigit()==False :
        choice = input("Enter a Positve number: ")
        
        if choice.isdigit()==False:
            print("Wrongly entered: ")
        else:
            return int(choice)




x = int(func())
print(x)

if (x == 2 or x == 0):
    print("Not Prime")
    sys.exit(1)
if x == 1:
    print("Not Prime")
    sys.exit(1)

for i in (range(2,x)):
    if x%i == 0:
        print("Not Prime")
        sys.exit(1)
    else:
        print("Prime")
        sys.exit(1)















