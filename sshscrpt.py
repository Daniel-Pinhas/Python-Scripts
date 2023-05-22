#!/usr/bin/python3

import sys
import paramiko
 

def usage():
    print("Bad usage")
    print("Usage:" + sys.argv[0] +"  Hostname"+"  Username"+"  Password"+"  Rcommand")

arglen = (len(sys.argv) -1)

if arglen != 4:
    usage()
    sys.exit(1)

hostname = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
Rcommand = sys.argv[4]



client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
                         
client.connect(hostname=hostname, port=22, username=username, password=password)

stdin, stdout, stderr = client.exec_command(Rcommand)
print(stdout.read().decode())
client.close()


