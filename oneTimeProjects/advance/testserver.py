import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.56.1', 9999))
print("Server hosted at %s:%d" %('192.168.56.1', 9999))
server.listen(5)
while True:
	# a = input()
	c, addr = server.accept()
	print("Connected to %s:%d" %(addr[0], addr[1]))
	print(c.recv(1024))
	print(c.send(b'ACK'))
	c.close()
server.close()