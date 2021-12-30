import socket

server = socket.socket()
server.connect(("192.168.0.103", 9999))
server.send(b'Hello')
print(server.recv(1024))