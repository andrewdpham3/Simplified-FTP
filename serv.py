#!/usr/bin/env python3

import socket
import sys
import argparse
import os

from libftp import *

# Create our argument parser object
parser = argparse.ArgumentParser(description='A simple FTP server.')

# Add our arguments to the parser
parser.add_argument("port", help="Port for the server to listen on")

# Make sure we have enough arguments, if not print the help message
if len(sys.argv) < 2:
	parser.print_help()
	sys.exit(1)

# Actually parse the arguments
args = parser.parse_args()

def get(settings, addr):
	sender_open(addr, settings[1])
	send_file(settings[0], data)

def put(settings, addr):
	listener_open(addr, settings[1])
	receive_file(settings[0])

try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind(('', int(args.port)))
		s.listen()
		print("Listening for client connections on port", args.port, "...")

		# Continuously accept incoming connections
		while True:

			print("Ready to accept connections...")
			conn, addr = s.accept()

			with conn:
				print("Accepted connection from", addr)

				conn_done = False

				while not conn_done:
					tmpdata = conn.recv(2)

					if not tmpdata:
						print("Client closed connection without sending a command!")
						conn_done = True
						break

					# Decode the control message as a UTF-8 string
					message = str(tmpdata.decode("utf-8"))

					if message[0] == "g":
						print("GET")
						get(control_get(conn), addr[0])

					elif message[0] == "p":
						print("PUT")
						filename = conn.recv(10).decode("utf-8")
						f = open(filename)
						data = sock.recv(1024)
						totalRecv = len(data)
						f.write(data.decode())
						while (sock.recv(1024)):
							data = s.recv(1024)
							totalRecv += len(data)
						f.write(data)
						f.close()

					elif message[0] == "l":
						print("LS")
						mySocket=socket.socket()
						mySocket.bind(("127.0.0.1",5000))
						mySocket.listen(1)
						connn, addr = mySocket.accept()
						data=os.listdir()
						str1 = '\n'.join(data)
						connn.send(str1.encode())

					elif message[0] == "q":
						print("Client disconnecting...")
						conn.close()
						conn_done = True

					else:
						print("Unknown Command:", message)
except KeyboardInterrupt:
	s.close()
	print()
	print("Exiting...")
	sys.exit(0)

except IOError as e:
	print("IOError: ", e)
	sys.exit(1)

except Exception as e:
	print("Something went wrong, but we don't know what!")
	print(e)
	sys.exit(1)
