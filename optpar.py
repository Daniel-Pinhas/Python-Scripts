#!/usr/bin/python3

import sys
import paramiko
import optparse

def usage():
    print("Bad usage")
    print("Usage:" + sys.argv[0] +"  Hostname"+"  Username"+"  Password"+"  Rcommand")

parser = optparse.OptionParser()
parser.add_option("--host", dest="hostname", help="Hostname for the SSH command")
parser.add_option("-u", "--username", dest="username", help="Username for SSH command")
parser.add_option("-p", "--password", dest="password", help="Password for SSH")
parser.add_option("-c", "--command", dest="command", help="Command to run")
(options, args) = parser.parse_args()

if not options.hostname or not options.username or not options.password or not options.command:
    parser.error("Missing required arguments")

hostname = options.hostname
username = options.username
password = options.password
Rcommand = options.command

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
client.connect(hostname=hostname, port=22, username=username, password=password)

stdin, stdout, stderr = client.exec_command(Rcommand)
print(stdout.read().decode())
client.close()








