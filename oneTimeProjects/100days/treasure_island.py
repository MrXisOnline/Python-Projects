print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
	''')

print("Welcome to treasure island\nYour mission is to find the treasure.")

def s_yellow():
	print("You entered the safezone. You Win!")


def s_red():
	print("You sliped from cliff. Game Over")


def s_blue():
	print("You enter a room of beasts. Game Over.")


def s_wait():
	print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and on blue. Which colour do you choose?")
	a=input()
	if a=="red":
		s_red()
	elif a=="yellow":
		s_yellow()
	elif a=="blue":
		s_blue()

def s_swim():
	print("A shark ate you. Game Over")


def s_right():
	print("You fell into a lava pool. Game Over")


def s_left():
	print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across")
	a=input()
	if a=="wait":
		s_wait()
	elif a=="swim":
		s_swim()


def start_game():
	print("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\"")
	a = input()
	if a=="left":
		s_left()
	elif a=="right":
		s_right()


start_game()