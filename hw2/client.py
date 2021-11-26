#!/bin/python3.8

# ref https://shengyu7697.github.io/python-tcp-socket/

import socket
import sys
from TimeLimit import time_limit, TimeoutException
from timeit import default_timer as timer

HOST = sys.argv[1]
PORT = int(sys.argv[2])
TIME = int(sys.argv[3])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


sendCount = 0

# 以time out 觸發signal ，關閉此function
def sendForever():
    outdata = bytes( bytearray(1000) )
    while True:
        # outdata = input('please input message: ')
        # print('send: ' , len(outdata))
        global sendCount
        sendCount += s.send(outdata)
        
        indata = s.recv(1024)
        if len(indata) == 0: # connection closed
            s.close()
            print('server closed connection.')
            break

# send data, limited by timeout
try:
    with time_limit(TIME):
        start = timer()
        sendForever()
except TimeoutException as e:
    print(f'send {sendCount/1000:.2f} KB  rate={sendCount/125/1000/TIME:.2f} Mbps')
    # print(e) # Timed out!
    pass

print( f"send for {timer()-start:.3f} seconds" )



