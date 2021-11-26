#!/bin/python3.8
# H py d.py 

from sys import argv  # argument error process
import sys


ERROR_MESSAGE = "Error: missing or additional arguments"
ERROR_PORT = "Error: port number must be in the range 1024 to 65535"

def error( message ):
    sys.exit( message )

mode=""
host=""
port=0
time=0

# check -c or -s exist
if "-c" in argv:
    mode+="client"
if "-s" in argv:
    mode+="server"

if "-h" in argv:
    host += argv[ argv.index("-h") + 1 ]

if "-p" in argv:  # get port integer
    port = int(argv[ argv.index("-p") + 1])

if "-t" in argv:
    time = argv[ argv.index("-t") + 1 ]

# check mode
if mode!="client" and mode!="server":
    error( ERROR_MESSAGE )

# c mode, check the host and time
if mode == "client":
    if time==0 or host=="":
        error( ERROR_MESSAGE )

# check port 
if  port < 1024 or  65535 < port:
    error(ERROR_PORT)

print(mode, host, port ,time)
    




