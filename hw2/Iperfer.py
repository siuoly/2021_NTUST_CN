#!/bin/python3.8
from argument import mode,port,host,time
import os

if(mode=="client"):
    os.system(f"python3 client.py {host} {port} {time}")
else:
    os.system(f"python3 server.py {port}")

