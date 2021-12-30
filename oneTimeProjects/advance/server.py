import socket
import decrypter
# from time import sleep

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created...")
socks.bind((socket.gethostname(), 9999))
socks.listen(5)
print("waiting for connections")
try:
	c, addr = socks.accept()
	print("accepted")
	name_enc = (c.recv(1024)).decode("utf-8")
	name_key = (c.recv(1024)).decode("utf-8")
	greet_enc = (c.recv(1024)).decode("utf-8")
	greet_key = (c.recv(1024)).decode("utf-8")
	pass_enc = (c.recv(1024)).decode("utf-8")
	pass_key = (c.recv(1024)).decode("utf-8")
	print("started decoding")
	print(name_enc, name_key)
	print(greet_enc, greet_key)
	name = decrypter.text_deco(name_enc, name_key)
	passwd = decrypter.text_deco(pass_enc, pass_key)
	greet = decrypter.text_deco(greet_enc, greet_key)
	print("Connected with ", name, "\nAdderess : ", addr[0], "Port No. : ", addr[1])
	print("Greets :", greet)
	print("password :",passwd)
	if passwd == "BHAI":
		msg = 'welcome to Community'
		c.send(msg.encode("utf-8"))
	else:
		msg = 'UNAUTHORISED'
		c.send(msg.encode("utf-8"))
	c.close()
except:
	print("closing server")
	socks.close()

