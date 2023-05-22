#!/usr/bin/python3
import datetime
import sys 

def usage():
    print("bad usage")
    print("usage: " + sys.argv[0] + " Name" + " Age" + "count of copies")

arglen = (len(sys.argv) -1)           

if arglen != 3:
    usage()
    sys.exit(1)

name = sys.argv[1]
age = sys.argv[2]
num = sys.argv[3]

x = int(age)
yearsleft = 100 - x
today = datetime.date.today().year
year = today + yearsleft 

w=0
while int(num) != w:
      w += 1
      print(name, "you will be 100 years old in", year) 




