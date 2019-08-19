# coding: utf-8

from socket import socket,AF_INET,SOCK_STREAM

s=socket(AF_INET,SOCK_STREAM)
s.connect(("",20000))
s.send(b'Hello')
while True:
	msg=s.recv(8192)
	if not msg:
		print(msg)
