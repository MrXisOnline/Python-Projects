def text_deco(data, key):
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

	return decoded_text