#! /usr/bin/python

import sys,socket

result=socket.getaddrinfo(sys.argv[1],None)
print(result)
