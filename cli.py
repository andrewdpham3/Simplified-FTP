# This will send text from a file to the server if its port is open

""" Commands that need to be implemented """
# ftp> get <file name> (downloads file <file name> from the server)

# ftp> put <filename> (uploads file <file name> to the server)

# ftp> ls(lists files on the server)

# ftp> quit(disconnects from the server and exits)

import socket
import os
import sys

PORT = 7001
HOST = '172.20.10.1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.connect((HOST,PORT))
	s.sendall(b'Hello, World!')
	reply = s.recv(1024)

print('Recieved')




"""
selection = input('Would you like to: \n1) upload a file to the server \n2) download a file from the server\n\n')

if int(selection) == 1:
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = input('Enter a file: ')
		upload.uploadFile(socket, filename)
elif int(selection) == 2:
	download.downloadFile(socket)

def downloadFile(socket):
	print('Downloading file')

def uploadFile(socket, filename):
	print('Uploading {0}'.format(filename))
"""