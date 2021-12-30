import time
import random

with open("words.txt", mode="r") as file:
	words = file.read()
words = words.split(", ")
start_time = time.time()
cur_word = random.choice(words).lower()
total_cor_word = 0
total_error = 0
while True:
	if time.time() - start_time <= 300:
		print(cur_word)
		inp = input()
		if cur_word == inp.split("\n")[0]:
			total_cor_word += 1
			cur_word = random.choice(words)
		else:
			total_error += 1
	else:
		break
print(f"Words Per Minute : {int(total_cor_word/5)}")
print(f"Total error : {total_error}")