#!/usr/bin/python3


file_path = input("Enter a file path: ")
print (file_path)

import sys
with open(file_path,'r', encoding='utf-8-sig') as i:
    lines = i.read()
    lst = []
    result = []
for x in open(file_path):
    lst.append(x)
    for x in lst:
        if x not in result:   
           result.append(x) 
print(str(len(result)) + (" Diffrent Names"))











