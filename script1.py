#!/usr/bin/python3


#x="daniel is 22 years old"

#print(x.upper())

#print(x[::-1])

#y=(len(x))
#print(y)

#z = (int(y/2))
#listx=([*x])
#print(listx)


#listx[z]="*"
#final="" .join(listx)
#print(final)

import sys
x = input("Enter a file: ")
f = open(x, "a")
f.write("Now the file has more content!")
f.close()





