# This will send text from a file to the server if its port is open

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