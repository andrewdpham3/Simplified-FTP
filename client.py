# This will send text from a file to the server if its port is open

import socket
import os
import sys

import upload
import download

port = 7001


socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

selection = input('Would you like to: \n1) upload a file to the server \n2) download a file from the server\n\n')

if int(selection) == 1:
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = input('Enter a file: ')
  upload.uploadFile(socket, filename)
elif int(selection) == 2:
  download.downloadFile(socket)
