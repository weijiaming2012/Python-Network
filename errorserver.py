#! /usr/bin/python

import socket,traceback

host=''  # bind to all interfaces
port=51432

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while True:
	try:
		clientsock,clientaddr=s.accept()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		continue

	# Process the connection
	
	try:
		print("Got connection from",clientsock.getpeername())
		# Process the request here
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc

	# Close the connection

	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
