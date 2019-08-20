#! /usr/bin/python

import socket

host=''   # Bind to all interfaces
port=51432

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
print("Waiting for connections...")
s.listen(1)

while True:
	clientsock,clientaddr=s.accept()
	print("Got connection from",clientsock.getpeername())
	clientsock.close()
