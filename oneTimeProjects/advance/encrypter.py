import random

alps = [
		"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
		"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
		]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def key_gen(key_len):
	key = ""
	for ran_char in range(key_len):
		key = key + random.choice(nums)

	return key


def text_enc(text, key_len=5):
	data = text.upper()
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
