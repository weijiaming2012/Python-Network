#! /usr/bin/python

import socket,traceback

host=''  # Bind to all interfaces
port = 51432

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))

while True:
	try:
		message,address=s.recvfrom(8192)
		print("Got data from",address)
		# Echo it back
		s.sendto(message,address)
	except (KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.pribt_exc()
