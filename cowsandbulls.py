#!/usr/bin/python3
import sys
import random

x = str(input("Enter 4 Digits Number: "))
while len(x) != 4:
    if (len(x) > 4) or (len(x) < 4):
        print(" You Must Enter 4 Digits!")
        x = str(input("Enter 4 Digits Number: "))

lst1 = []

while len(lst1) != 4:
    z=(random.randint(0,9))
    lst1.append(z)
lst2 = []

for i in range(len(lst1)):
    if (int(lst1[i])) == (int(x[i])):
        lst2.append("cow")  
    else:
        lst2.append("bull")
bull = (str(lst2.count("bull")))
cow = (str(lst2.count("cow"))) 
print(cow + " Cows")
print(bull + " Bulls")


while True:
    if cow == "4":
        print("Good Job! You Got The 4 Bulls!")
        print("You Guessed "  " Times")
        sys.exit(1)
    x = str(input("Enter 4 Digits Number: "))
    while len(x) != 4:
        if (len(x) > 4) or (len(x) < 4):
            print(" You Must Enter 4 Digits!")
            x = str(input("Enter 4 Digits Number: "))
    for i in range(len(lst1)):
        if (int(lst1[i])) == (int(x[i])):
            lst2[i] = ("cow")  
        else:
            lst2[i] = ("bull")

    bull = (str(lst2.count("bull")))
    cow = (str(lst2.count("cow"))) 
    print(cow + " Cows")
    print(bull + " Bulls")
    
   
      
    


    
     