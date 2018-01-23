#!/usr/bin/env python

import socket
import math      

while 1:
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5016
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()

    print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    print "factoridal data:", math.factorial(int(data))

    conn.send(str(math.factorial(int(data))))  # echo

