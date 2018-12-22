#!/usr/bin/env python3

import socket
import sys
import argparse

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
					data = conn.recv(1)

					if not data:
						# FIXME: Client closed connection
						print("Panic")
						sys.exit(1)

					# Decode the control message as a UTF-8 string
					message = str(data.decode("utf-8"))

					if message == "g":
						print("GET")

					elif message == "p":
						print("PUT")

					elif message == "l":
						print("LS")

					elif message == "q":
						print("Client disconnecting...")
						conn.close()
						conn_done = True

					else:
						print("Unknown Command:", message)
						# TODO: send uc
except KeyboardInterrupt:
	print("Exiting...")
	sys.exit(0)
except IOError as e:
	print("IOError: ", e)
	sys.exit(1)
except:
	print("Something went wrong, but we don't know what!")
	sys.exit(1)
