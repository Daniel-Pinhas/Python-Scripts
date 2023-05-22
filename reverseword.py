#!/usr/bin/python3

string = "My name is Dora"

y = string.split(" ")
z= len(y) -1
lst = []
x = 0
while z - x >= 0: 
    lst.append(y[z - x])
    x += 1 
print (' '.join(lst)) 




















