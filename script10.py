#!/usr/bin/python3

import sys

def usage():
    print("Bad usage")
    print("Usage: " + sys.argv[0] + " file" + " file2")

arglen = (len(sys.argv) -1)           

if arglen != 2:
    usage()
    sys.exit(1)

file1 = sys.argv[1] 
file2 = sys.argv[2]

f1 = open(file1 , "r" )
f2 = open(file2 , "r" )

lst1=[]
lst2 = []
result = [] 
for num1 in f1:
    lst1.append(int(num1))
for num2 in f2:
    lst2.append(int(num2))
    for n in lst1:
        if int(n) in lst2:
            result.append(int(n)) 
print(set(result))

f1.close()
f2.close()