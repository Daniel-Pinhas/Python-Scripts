#!/usr/bin/python3
import re
import glob
import sys

def usage():
    print("Bad usage")
    print("Usage:   " + sys.argv[0] + "  file" + "  word")

arglen = (len(sys.argv) -1)

if arglen != 2:
    usage()
    sys.exit(1)

file1 = sys.argv[1]
word = sys.argv[2]


with open(file1,"r") as file_one:
    for line in file_one:
        if re.search(word, line):
            print(line)

regexp = re.compile(file1)
for arg in sys.argv[2:]:
    for fn in glob.iglob(arg):
        with open(fn) as file:
            for line in file:
                if re.search(regexp, line):
                    print(line, end='')








