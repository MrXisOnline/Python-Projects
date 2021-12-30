import random

alps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
syms = ["!", '+', '#', '$', '%', '&', '*', '(', ')']
print("Welcome to the PyPassword Generator!")
pass_length = int(input("How many letters would you like in your password?\n"))
sym_num = int(input("How many symbols would you like?\n"))
num_num = int(input("How many numbers would you like?\n"))
total_length= pass_length+sym_num+num_num
passcode = ''
pos_sym = []
for j in range(0,sym_num):
	pos_sym.append(random.randint(1,total_length))

pos_num = []
for k in range(0, num_num):
	pos_num.append(random.randint(1,total_length))
	if pos_num[k] in pos_sym:
		pos_num.append(random.randint(1,total_length))

for i in range(0,total_length):
	if i in pos_sym:
		char = random.choice(syms)
		passcode = passcode + char
	elif i in pos_num:
		char = random.choice(nums)
		passcode = passcode + char
	else:
		char = random.choice(alps)
		passcode = passcode + char

print(f"Here is your password: {passcode}")