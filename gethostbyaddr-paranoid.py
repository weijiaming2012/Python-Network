#! /usr/bin/python

import socket,sys

def getipaddrs(hostname):
	result=socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
	return [x[4][0] for x in result]

def gethostname(ipaddr):
	return socket.gethostbyaddr(ipaddr)[0]

try:
	hostname=gethostname(sys.argv[1])
	ipaddrs=getipaddrs(hostname)
except socket.herror as e:
	print("No host names")
	sys.exit(0)
except socket.gaierror as e:
	print("Got hostname")
	sys.exit(1)

if sys.argv[1] not in ipaddrs:
	print("not in ipaddrs")
	sys.exit(1)

print("Validated hostname:{}".format(hostname))
