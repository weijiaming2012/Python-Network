#! /usr/bin/python

import sys,socket

result=socket.getaddrinfo(sys.argv[1],None)

counter=0
for item in result:
	print("%-2d:%s" % (counter,item[-1]))
	counter+=1
