#! /usr/bin/python

import socket 

print "Creating socket..."
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "done."

print "Looking up port number..."
port=socket.getservbyname('http','tcp')
print port
print "done."

print "Connecting to remote host..."
s.connect(("www.baidu.com",80))
print "done."
