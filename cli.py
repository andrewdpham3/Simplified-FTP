#!/usr/bin/env python3

import socket
import os
import sys

if len(sys.argv) < 2:
	raise TypeError('cli.py was not called correctly. cli <server machine> <server port>')
else:
	server_machine = sys.argv[0]
	server_port = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.connect((server_machine,server_port))

	print('FTP>')
	command = input('')
	decodeInput(command)



def decodeInput(user_input):
	""" Will translate user input to proper client command
	@param input: user input string
	"""
	user_input = user_input.upper()

	if user_input == 'GET':
		downloadFile()
	else if user_input == 'PUT':
		uploadFile()
	else if user_input == 'LS':
		listFiles()
	else if user_input == 'QUIT':
		quit()
	else:
		print('The command "{0}" is not recognized. Try again.')

def downloadFile(socket):
	""" Will perform a download"""
	print('Downloading file')

def uploadFile(socket, filename):
	""" Will perform an upload """
	print('Uploading {0}'.format(filename))

def listFiles(socket):
	""" Will list files on the server """
	pass

def quit(socket):
	""" Will Disconnect from the Server and Exit """
	pass


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

'''
selection = input('Would you like to: \n1) upload a file to the server \n2) download a file from the server\n\n')

if int(selection) == 1:
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = input('Enter a file: ')
		upload.uploadFile(socket, filename)
elif int(selection) == 2:
	download.downloadFile(socket)
'''
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
