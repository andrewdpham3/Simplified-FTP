#!/usr/bin/env python3
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

control.connect((args.address, int(args.port)))


################# Command Definitions ######################

def get(filename):
	""" Downloads file from the server """
	print('Downloading file:', filename)
	port = random.randint(6000,7000)
	message = bytes(("g;" + filename + ";" + str(port) + "\r\n"), "utf-8")
	control.sendall(message)
	s = listener_open(port)
	receive_file(filename,s)


def put(filename):
	""" Uploads file to the server """
	print('Uploading file:', filename)
	port = random.randint(6000,7000)
	s = sender_open(port)
	send_file(filename,s)


def ls(directory):
	""" List files on the server """ 
	print('Listing files on server...')
	port = random.randint(6000,7000)
	s = listener_open(port)
	ls_files(directory,s)

done = False

try:
	while not done:
		command = input("ftp> ").split()
		command = command.upper()

		if command[0] == 'GET':
			get(command[1])

		elif command[0] == 'PUT':
			put(command[1])

		elif command[0] == 'LS':
			ls(command[1])

		elif command[0] == 'QUIT':
			control.close()
			done = True

		else:
			print()
			print('The command "{}" is not recognized '.format(command[0]))
			print("Please use one of the following commands:")
			print("get <filename>")
			print("put <filename>")
			print("ls <directory>")
			print("quit")

except KeyboardInterrupt:
	print()
	print("Exiting...")
	sys.exit(0)
