import sys
import random

def check_space(string):
	for char in range(len(string)):
		if string[char] == " ":
			return char

def prime_checker(number):
	n = 0
	for i in range(2,number):
		if number%i == 0:
			n = n + 1

	if n == 0:
		return True
	else:
		return False


def check_int(string):
	try:
		return int(string)
	except:
		print("[-] Input Integer Only!!!")
		sys.exit(0)

def generate_clue(number):
	clue_type = ["mul", "divi", "grt", "sml"]
	ran_type = random.choice(clue_type)
	if ran_type == "mul":
		if prime_checker(number):
			return "Prime Number"

		if number%2==0:
			return "Multiple Of 2"
		elif number%5==0:
			return "Multiple Of 5"
	elif ran_type == "divi":

		if number%2 == 0:
			return "Divisible By 2"
		elif number%5 == 0:
			return "Divisible By 5"
	elif ran_type == "grt" or ran_type == "sml":
		if number > 5:
			return "Greater Than 5"
		else:
			return "Smaller Than 5"


def enter_level(level):
	score = 0

	if level > 3:
			print("[-] Input Between (1,2,3)")
			sys.exit(0)

	if level == 1:
		while True:

			if score > 4:
				print("Promoted to Level 2")
				enter_level(2)

			try:
				print("[CTRL-C To Stop]")
				random_num = random.randint(1, 10)
				print("Your Clue Is %s" %generate_clue(random_num))
				guess = check_int(input("Guess the Number Between 1-10 ->>"))
				if guess == random_num:
					print("\nCorrect\n")
					score = score + 2
				else:
					print("\nNope\n")
					score = score - 1
			except KeyboardInterrupt:
				break

		print("Your Score :%d" %score)
		sys.exit(0)
	elif level == 2:
		while True:

			if score > 20:
				print("Promoted to Level 3")
				enter_level(3)

			try:
				print("[CTRL-C To Stop]")
				random_num = random.randint(1, 100)
				print("Your Clue Is %s" %generate_clue(random_num))
				guess = check_int(input("Guess the Number Between 1-100 ->>"))
				if guess == random_num:
					print("\nCorrect\n")
					score = score + 5
				else:
					print("\nNope\n")
					score = score - 1
			except KeyboardInterrupt:
				break

		print("Your Score :%d" %score)
		sys.exit(0)
	elif level == 3:
		try:
			ran = input("Enter Range [x y] ->")
			space_pos = check_space(ran)
			start = check_int(ran[0:space_pos])
			end = check_int(ran[space_pos+1:len(ran)])
			while True:
				try:
					print("[CTRL-C To Stop]")
					random_num = random.randint(start, end)
					print("Your Clue Is %s" %generate_clue(random_num))
					guess = check_int(input("Guess the Number Between %d-%d ->>" %(start,end)))
					if guess == random_num:
						print("\nCorrect\n")
						score = score + 5
					else:
						print("\nNope\n")
						score = score - 1
				except KeyboardInterrupt:
					print()
					print("Your Score :%d" %score)
					break
					sys.exit(0)
		except KeyboardInterrupt:
			print("Your Score :%d" %score)
			sys.exit(0)



print("Guess The Number Game".center(50,"-"))
level = check_int(input("Which Level You Want To Play (1,2,3) ->>"))
enter_level(level)




