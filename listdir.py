#!/usr/bin/python3
import sys
import os
import hashlib
import csv

def usage():
    print("Bad usage")
    print("Usage:   " + sys.argv[0] + "  Directory" + "  File Path")

arglen = (len(sys.argv) -1)

if arglen != 2:
    usage()
    sys.exit(1)

dir = sys.argv[1]
file_path = sys.argv[2]

if os.path.isdir(dir):
    print((dir) + " is a Directory")
else:
    print((dir) + " is not a Directory")

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
list_files(dir)

md5 = (hashlib.md5(open(file_path,'rb').read()).hexdigest())

with open(file_path, 'r') as fp:
    for count, line in enumerate(fp):
        pass
    x= ( count + 1)

if __name__ == '__main__':
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(((x),(file_path),(md5)))           




