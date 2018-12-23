import socket
import sys

# Read data from the control channel and return a tuple of arguments
def control_get(conn):
	partial = ""

	# Get the filename
	while True:
		data = conn.recv(16)

		if not data:
			# FIXME: Client closed connection
			print("Panic")
			break
		else:
			partial += str(data.decode("utf-8"))

		end = partial.find("\r\n")
		if end > 0:
			partial = partial[:end]
			break

	return partial.split(";")

# Open and return a data channel connection
def sender_open(addr, port):
	try:
		print("addr:", addr)
		with socket.create_connection((str(addr), port)) as s:
			return s
	except IOError as e:
		print("IOError while opening sender channel: ", e)
		sys.exit(1)

# Open and return a data channel connection and address object
def listener_open(port=None):
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			if not port:
				s.bind(('', 0))
			else:
				s.bind(('', port))
			s.listen()
			conn, addr = s.accept()

			# TODO: do we need to close this?
			s.close()

			return (conn, addr, s.getsockname()[1])
	except IOError as e:
		print("IOError while opening listener channel: ", e)
		sys.exit(1)

# Send a file over a socket
def send_file(filename, sock):
	with open(filename, 'rb') as f:
		print("Sending file", filename, "...")
		
		block = f.read(1024)
		while (block):
			sock.send(block)
			block = f.read(1024)
		f.close()
		sock.close()

# Receive a file over a socket
def receive_file(filename, sock):
	with open(filename, 'wb') as f:
		print("Receiving file", filename, "...")
		
		block = sock.recv(1024)
		while (block):
			f.write(block)
			block = sock.recv(1024)
		f.close()
		sock.close()
