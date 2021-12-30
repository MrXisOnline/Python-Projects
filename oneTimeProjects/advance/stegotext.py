import sys
import getopt
import os
import random


os.chdir("C:\\Users\\SG704\\PythonProjects\\oneTimeProjects\\advance")

# Global Variables
target = ""
output = "output.txt"
key = ""
key_length = 5
crypt = True
alps = [
		"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
		"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
		]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def usage():
	print ("StegoText Crypt Tool")
	print()
	print("Usage: stegotext.py -c -t target-file")
	print("-o --output -setup output file name")
	print("-k --key -setup key length")
	print()
	print()
	print("Examples: ")
	print("stegotext.py -c -t secrettext.txt")
	print("stegotext.py -c -t secrettext.txt -o cyphertext.txt")
	print("stegotext.py -c -t secrettext.txt -o cyphertext.txt -k 4")
	sys.exit(0)

def key_gen(key_len):
	global key
	for ran_char in range(key_len):
		key = key + random.choice(nums)

	return key


def crypt_text(target_file, key):
	open_target_file = open(target_file, "r")
	dt = open_target_file.read()
	data = dt.upper()
	open_target_file.close()
	encoded_text = ""
	key_len_char = 0
	for exe in range(len(data)):
		if key_len_char == len(key):
			key_len_char = 0

		for sub_exe in range(int(key[key_len_char])-1):
			encoded_text = encoded_text + random.choice(alps)

		encoded_text = encoded_text + data[exe]
		key_len_char = key_len_char + 1	

	return encoded_text		


def decrypt_text(target_file, key):
	open_target_file = open(target_file, "r")
	data = open_target_file.read()
	open_target_file.close()
	decoded_text = ""
	key_len_char = 0
	key_history = 0
	key_len_char = key_len_char + int(key[key_history]) - 1
	
	for exe in range(len(data)):
		# print(exe)
		if exe == key_len_char:
			decoded_text = decoded_text + data[exe]
			key_history = key_history + 1
			if key_history == len(key):
				key_history = 0
			
			key_len_char = key_len_char + int(key[key_history])

	print("decoded Text : \t%r" %decoded_text)
	return 0


def send_data(encoded_text, output_file):
	if output_file == "output.txt":
		try:
			open_output_file = open(output_file, "x")
			open_output_file.write(encoded_text)
			open_output_file.close()
		except Exception as e:
			print("output.txt Already Exists")
			sys.exit(0)
	else:
		try:
			open_output_file = open(output_file, "x")
			open_output_file.write(encoded_text)
			open_output_file.close()
		except Exception as e:
			print("Error Occured")
			print(str(e))
			sys.exit(0)

	return 1


def text_enc(text, key_len=5):
	key = key_gen(key_len)
	encoded_text = ""
	key_len_char = 0
	for exe in range(len(data)):
		if key_len_char == len(key):
			key_len_char = 0

		for sub_exe in range(int(key[key_len_char])-1):
			encoded_text = encoded_text + random.choice(alps)

		encoded_text = encoded_text + data[exe]
		key_len_char = key_len_char + 1	

	return encoded_text, key


def main():
	global output
	global target
	global key_length
	global key
	global crypt

	if not len(sys.argv[1:]):
		usage()

	# read the commandline options
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hkcdz:t:o:", ["help","key","crypt","decrypt","decryptkey","target","output"])
	except getopt.GetoptError as err:
		print(str(err))
		usage()


	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-k","--key"):
			key_length = int(a)
		elif o in ("-t", "--target"):
			target = a
		elif o in ("-c", "--crypt"):
			crypt = True
		elif o in ("-d", "--decrypt"):
			crypt = False
		elif o in ("-o", "--output"):
			output = a
		elif o in ("-z", "--decryptkey"):
			key = a
		else:
			assert False,"Unhandled Option"

	if crypt == True:
		key = key_gen(key_length)
		cypher = crypt_text(target, key)
		print(cypher)
		print("Sending to output file...")
		send = send_data(cypher, output)

		if send == 1:
			print("Saved the cypher to output file")
			print("Your Decrypt-Key :", key)

	else:
		decrypt_text(target, key)


main()