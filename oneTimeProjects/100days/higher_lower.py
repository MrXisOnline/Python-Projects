from higher_lower_data import data
from os import system
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def start_game(score=0):
	run = True
	counter = 0
	while run:
		if counter > 0:
			data_index = sec_index
			sec_index = random.randint(0,len(data) - 1)
		else:
			data_index = random.randint(0,len(data) - 1)
			sec_index = random.randint(0,len(data) - 1)
			counter += 1

		if data_index == sec_index:
			start_game(score)

		system("cls")
		print(logo)
		if data_index == len(data):
			print("You Won The Game!")
			break
		elif score > 0:
			print(f"You\'re right! Current score: {score}.")

		print(f"Compare A: {data[data_index]['name']}, {data[data_index]['description']}, from {data[data_index]['country']}.")
		print(vs)
		print(f"Against B: {data[sec_index]['name']}, {data[sec_index]['description']}, from {data[sec_index]['country']}.")
		comp_in = input("Who has more followers? Type \'A\' or \'B\': ").upper()
		if comp_in == "A":
			if data[data_index]["follower_count"] > data[sec_index]["follower_count"]:
				score += 1
			else:
				run =False
		elif comp_in == "B":
			if data[sec_index]["follower_count"] > data[data_index]["follower_count"]:
				score += 1
			else:
				run =False
		else:
			print("Wrong Option!")
			run = False
	else:
		print(f"You lose! Current score: {score}.")


start_game()