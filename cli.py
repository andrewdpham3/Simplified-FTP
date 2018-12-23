import socket
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

s = sender_open(args.address, args.port)

def get(filename):
	print("Getting file:", filename)
	# TODO: actually download the file

#TODO: put, ls

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
			# TODO: send close
			s.close()
			done = True

		else:
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
