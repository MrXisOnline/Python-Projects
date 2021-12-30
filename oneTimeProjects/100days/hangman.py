import random

def game_art():
	print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
		''')

game_art()

hang_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ["fireboard", "identical", "beekeeper", "chocolate", "computers", "christmas"]
ran_word = random.choice(words)
sh_list = ["_" for i in ran_word]
hints = len(ran_word) - 2
hang = 0
while hints > 0:
	if "_" in sh_list:
		print()
		char = input("Choose A Chracter : ")
		if char in ran_word:
			char_index=[]
			for i in range(len(ran_word)):
				if char == ran_word[i]:
					char_index.append(i)
			for j in char_index:
				sh_list[j] = ran_word[j]
			print()
			for k in sh_list:
				print(k, end=' ')
			print()
		else:
			hints -= 1
			print(hang_stages[hang])
			hang += 1
			print()
			print("Wrong Character!")
			print()
			print(f"Remaining Hints : {hints}")
	else:
		print()
		print("You Win")
		break
else:
	print()
	print("You Lose!")