#!/usr/bin/env python3

import socket
import random
import sys
import argparse

from libftp import *

# Create our argument parser object
parser = argparse.ArgumentParser(description='A simple FTP client.')

# Add our arguments to the parser
parser.add_argument("address", help="Address of the server.")
parser.add_argument("port", help="Port to connect to the server with.")

# Make sure we have enough arguments, if not print the help message
if len(sys.argv) < 3:
	parser.print_help()
	sys.exit(1)

# Actually parse the arguments
args = parser.parse_args()

done = False

control.connect((args.address, int(args.port)))

def get(filename):
	print("Getting file:", filename)
	port = random.randint(6000,7000)
	message = bytes(("g;" + filename + ";" + str(port) + "\r\n"), "utf-8")
	control.sendall(message)
	s = listener_open(port)
	receive_file(filename, s)

#TODO: put

#TODO: ls

try:
	while not done:
		command = input("ftp> ").split()

		if command[0] == "get":
			get(command[1])

		elif command[0] == "put":
			put(command[1])

		elif command[0] == "ls":
			ls(command[1])

		elif command[0] == "quit":
			control.close()
			done = True

		else:
			print()
			print("Unknown command entered!")
			print("Please use one of the following commands:")
			print("get <filename>")
			print("put <filename>")
			print("ls <directory>")
			print("quit")

except KeyboardInterrupt:
	print()
	print("Exiting...")
	sys.exit(0)
