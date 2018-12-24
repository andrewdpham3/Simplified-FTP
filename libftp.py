import socket
import sys
import os

control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Read data from the control channel and return a tuple of arguments
def control_get(conn):
	partial = ""

	while True:
		print("recving data...")
		tmpdata = conn.recv(16)

		if not tmpdata:
			print("Client closed connection while we were receiving data!")
			break
		else:
			partial += str(tmpdata.decode("utf-8"))
		print(partial)

		end = partial.find("\r\n")
		if end > 0:
			partial = partial[:end]
			break

	return partial.split(";")

# Open and return a data channel connection
def sender_open(addr, port):
	try:
		print("Opening sender channel to", addr, port, "...")
		data.connect((addr, int(port)))
	except IOError as e:
		print("IOError while opening sender channel: ", e)
		sys.exit(1)

# Open and return a data channel connection and address object
def listener_open(port):
	try:
		data.bind(('', port))
		print("Listening on port", port, "...")
		data.listen()
		conn, addr = data.accept()

		#data.close()

		#return conn

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

'''# Receive a file over a socket
def receive_file(filename, sock):
	with open(filename, 'wb') as f:
		print("Receiving file", filename, "...")
		
		block = sock.recv(1024)
		while (block):
			f.write(block)
			block = sock.recv(1024)
		f.close()
		sock.close()
'''
def receive_file(filename,sock):
	f = open('new_'+filename, 'w+')
	data = sock.recv(1024)
	totalRecv = len(data)
	f.write(data.decode())
	while (sock.recv(1024)):
		data = s.recv(1024)
		totalRecv += len(data)
		f.write(data)
	f.close()

def send_ls(sock):
	print("send ls called")
	sock.send(os.listdir())

def ls_files(sock):
	print("ls files called")
	print(sock.receive(1024))