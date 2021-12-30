import socket
import sys
import threading

def check_client(cli_sock):
	user_enc = cli_sock.recv(1024)
	passwd_enc = cli_sock.recv(1024)
	user = user_enc.decode("utf-8")
	passwd = passwd_enc.decode("utf-8")
	if user == "USER jms" and passwd == "PASS 123":
		cli_sock.send("AUTH".encode("utf-8"))
		cli_sock.close()
	else:
		cli_sock.send("DEAUTH".encode("utf-8"))
		cli_sock.close()

host = "192.168.56.1"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, 110))
server.listen(2)
print("Server Started at %s" %host)

try:
	while True:
		cli_sock, addr = server.accept()
		th = threading.Thread(target=check_client,args=(cli_sock,))
		th.start()

except KeyboardInterrupt:
	sys.exit(0)
