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
