#! /usr/bin/python

import socket,sys

def getipaddrs(hostname):
	result=socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
	return [x[4][0] for x in result]

hostname=socket.gethostname()
print("Host name:{}".format(hostname))

print("Fully-qualified name:{}".format(socket.getfqdn(hostname)))
try:
	print(getipaddrs(hostname))
except socket.gaierror as e:
	print(e)
