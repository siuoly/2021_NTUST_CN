#!/bin/python3.8
import socket
import sys
import time

HOST = '0.0.0.0'
PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(( HOST, PORT ))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    # connection, address
    conn, addr = s.accept()

    # 顯示連進來的 client 資訊
    print('connected by ' + str(addr))
    start = time.perf_counter()

    # receive bytes 
    recvCount = 0
    while True:
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()

            pass_time = time.perf_counter() - start  # 
            print('client closed connection.')
            print( f'received={recvCount/1000} KB rate={recvCount/125000/pass_time:.2f} Mbps')
            break
        # print('recv: ' , len(indata))
        recvCount += len(indata)

        outdata = 'serve recv ' + str(len(indata)) + 'bytes'
        conn.send(outdata.encode())


