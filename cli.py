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
	#port = "1234"
	message = bytes(("p;" + filename + ";" + str(port) + "\r\n"), "utf-8")
	control.sendall(message)
	s = sender_open("127.0.0.1",port)#todo: un-hardcode the localhost
	send_file(filename,s)


def ls():
	""" List files on the server """ 
	print('Listing files on server...')
	port = 5000
	message = bytes(("l;"), "utf-8")
	control.sendall(message)
	mySocket = socket.socket()
	mySocket.connect(('127.0.0.1',port))
	data = mySocket.recv(1024).decode()
	print(data)


done = False

try:
	while not done:
		command = input("ftp> ").split()
		cmd = command[0].upper()

		if cmd == 'GET':
			get(command[1])

		elif cmd == 'PUT':
			put(command[1])

		elif cmd == 'LS':
			ls()

		elif cmd == 'QUIT':
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