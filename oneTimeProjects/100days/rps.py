import random

def rock():
	print("""
	    _______
	---'   ____)
	      (_____)
	      (_____)
	      (____)
	---.__(___)
	""")

def paper():
	print("""
	     _______
	---'    ____)____
	           ______)
	          _______)
	         _______)
	---.__________)
	""")

def scissor():
	print("""
	    _______
	---'   ____)____
	          ______)
	       __________)
	      (____)
	---.__(___)
	""")

def art_printer(imp):
	if imp == 0:
		rock()
	elif imp == 1:
		paper()
	else:
		scissor()


game_elements = ["rock","paper","scissor"]
print("Choose 0 for rock, 1 for paper, 2 for scissor")
usr_in = int(input())
print(f"You choose {game_elements[usr_in]}")
art_printer(usr_in)
com_in = random.randint(0,2)
print(f"Computer choose {game_elements[com_in]}")
art_printer(com_in)

if usr_in == com_in:
	print("DRAW")
elif usr_in == 0:
	if com_in == 1:
		print("YOU LOSE")
	elif com_in == 2:
		print("YOU WIN")
elif usr_in == 1:
	if com_in == 0:
		print("YOU WIN")
	elif com_in == 2:
		print("YOU LOSE")
else:
	if com_in == 0:
		print("YOU LOSE")
	elif com_in == 1:
		print("YOU WIN")


