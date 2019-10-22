#! /usr/bin/python

import socket,sys

try:
	result=socket.gethostbyaddr(sys.argv[1])

	print("Primary hostname:{}".format(result[0]))


	print("\nAddress:")
	for item in result[2]:
		print(" {}".format(item))

	print(result)

except socket.herror as e:
	print(e)
