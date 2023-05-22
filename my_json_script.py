#!/usr/bin/python3

import sys
from collections import Counter
import json


def usage():
    print("Bad usage")
    print("Usage: " + sys.argv[0] + " String")

arglen = (len(sys.argv) -1)           
string = sys.argv[1] 

if arglen != 1:
    usage()
    sys.exit(1)


lst = list(string)
print(Counter(lst))

with open("dictionar.json", "a") as outfile:
    json.dump(str(Counter(lst)) , outfile)

