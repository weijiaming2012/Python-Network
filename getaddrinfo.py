#! /usr/bin/python

import socket,sys

host,port=sys.argv[1:]
results=socket.getaddrinfo(host,port,0,socket.SOCK_STREAM)

for result in results:
	print("-"*60)

	if result[0]==socket.AF_INET:
		print("Family:AF_INET")
	elif result[0]==socket.AF_INET6:
		print("Family:AF_INET6")
	else:
		print("Family:{}".format(result[0]))

	if result[1]==socket.SOCK_STREAM:
		print("Socket Type:SOCK_STREAM")
	elif result[1]==socket.SOCK_DGRAM:
		print("Socket Type:SOCK_DGRAM")

	print("Protocol:{}".format(result[2]))
	print("Canonical Name:{}".format(result[3]))
	print("Socket Address:{}".format(result[4]))
