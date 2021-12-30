def get_separate(text):
	seprate_text = []
	for i in range(len(text)):
		seprate_text.append(text[i])
	return seprate_text


def get_enc_char(char,shift):
	index=0
	alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in range(len(alps)):
		if char == alps[i]:
			index = i
			break
	full_index = index + shift
	print(full_index)
	if full_index >= 26:
		return alps[full_index-26]
	else:
		return alps[full_index]


def get_dec_char(char,shift):
	alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	index=0
	for i in range(len(alps)):
		if char == alps[i]:
			index = i
			break
	real_index = index - shift
	return alps[real_index]



def encode_text(text,shift):
	separate_text = get_separate(text.lower())
	enc_text = ""
	alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in separate_text:
		if i in alps:
			enc_text = enc_text + get_enc_char(i,shift)
		else:
			enc_text = enc_text + i
	return enc_text


def decode_text(enc_text,shift):
	alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	separate_text = get_separate(enc_text)
	dec_text = ""
	for i in separate_text:
		if i in alps:
			dec_text = dec_text + get_dec_char(i,shift)
		else:
			dec_text = dec_text + i
	return dec_text



art = '''
                                        _  _  _ __  _              
 __  __ _  ___  ___ ___  _ _        __ | || || '_ \| |_   ___  _ _ 
/ _|/ _` |/ -_)(_-// -_)| '_|      / _| \_. || .__/|   \ / -_)| '_|
\__|\__/_|\___|/__/\___||_|        \__| |__/ |_|   |_||_|\___||_|  

'''

print(art)
run = True
while run:
	operation = input("Type \'encode\' to encrypt, type \'decode\' to decrypt :\n").lower()
	if operation == "encode":
		message = input("Type your message:\n")
		shift_key = int(input("Type the shift number:\n"))
		enc_text = encode_text(message,shift_key)
		print(f"Here\'s the encoded result: {enc_text}")
		cont = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.\n").lower()
		if cont == "yes":
			continue
		elif cont == "no":
			run = False
		else:
			print("Wrong string")
	elif operation == "decode":
		message = input("Type your message:\n")
		shift_key = int(input("Type the shift number:\n"))
		dec_text = decode_text(message,shift_key)
		print(f"Here\'s the encoded result: {dec_text}")
		cont = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.\n").lower()
		if cont == "yes":
			continue
		elif cont == "no":
			run = False
		else:
			print("Wrong string")
	elif operation == "exit":
		print("Exiting Program...")
		run = False
	else:
		print("Wrong Operation!")