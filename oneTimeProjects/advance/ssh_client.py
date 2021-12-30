import socket
import encrypter
from time import sleep

def send_recv_command(server_socket):
	try:
		while True:
			command = input("Command to execute :")
			command_opt = ""
			server_socket.send(command.encode("utf-8"))
			data_len=1
			while data_len > 0:
				dt = server_socket.recv(4096)
				data = dt.decode("utf-8")
				data_len = len(dt)
				command_opt = command_opt + data

				if data_len < 4096:
					break

			print(command_opt)
	except:
		print("Server Stopped!!!")
		server_socket.close()


server = socket.socket()
server.connect(("192.168.56.1", 9999))
username = input("Username :")
password = input("Password :")
user_enc, user_enc_key = encrypter.text_enc(username)
pass_enc, pass_enc_key = encrypter.text_enc(password)
sleep(1)
server.send(user_enc.encode("utf-8"))
sleep(1)
server.send(user_enc_key.encode("utf-8"))
sleep(1)
server.send(pass_enc.encode("utf-8"))
sleep(1)
server.send(pass_enc_key.encode("utf-8"))
sleep(3)
res = server.recv(1024)
auth = res.decode("utf-8")
print(auth)
sleep(1)

if auth == "Authenticated":
	send_recv_command(server)

server.close()