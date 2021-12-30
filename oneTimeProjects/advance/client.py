import socket
from time import sleep
import encrypter

try:
	client = socket.socket()

	client.connect(("192.168.56.1", 9999))
	name = input("Your name : ")
	enc_name, name_key = encrypter.text_enc(name)
	print(enc_name)
	passwd = input("Your Password : ")
	enc_pass, pass_key = encrypter.text_enc(passwd)
	print(enc_pass)
	greet = input("Your greets : ")
	enc_greet, greet_key = encrypter.text_enc(greet)
	print(enc_greet)
	print("Started sending")
	sleep(1)
	client.send(enc_name.encode("utf-8"))
	sleep(1)
	client.send(name_key.encode("utf-8"))
	sleep(1)
	client.send(enc_greet.encode("utf-8"))
	sleep(1)
	client.send(greet_key.encode("utf-8"))
	sleep(1)
	client.send(enc_pass.encode("utf-8"))
	sleep(1)
	client.send(pass_key.encode("utf-8"))
	sleep(3)
	print("Started recv")
	# client.send(bytes(name, "utf-8"))
	print((client.recv(1024)).decode("utf-8"))
except:
	client.close()
