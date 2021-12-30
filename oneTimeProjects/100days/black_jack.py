import random
from os import system

def card_chooser():
	cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
	client_cards = []
	your_cards = []
	for i in range(2):
		client_cards.append(random.choice(cards))
		your_cards.append(random.choice(cards))
	return your_cards, client_cards

run = True
art = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
'''
def score(card):
	sre = 0
	for i in card:
		if i in ["J", "Q", "K"]:
			sre = sre + 10
		elif i == "A":
			sre = sre + 11
		else:
			sre = sre + i
	return sre


while run:
	print(art)
	cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
	if input("Wants to continue enter \'y\' or \'n\': ") == 'y':
		you, client = card_chooser()
		your_score = score(you)
		client_score = score(client)
		print(f"\tYour cards : {you}, current score: {your_score}")
		print(f"\tComputer\'s first card: {client[0]}")
		cont = input("Type \'y\' to get another card, type \'n\' to pass: ")
		if cont == "y":
			you.append(random.choice(cards))
			if client_score < 17:
				client.append(random.choice(cards))
		your_score = score(you)
		client_score = score(client)
		if (your_score > 21) and ("A" in you):
			ins = you.index("A")
			you[ins] = 1
			your_score = score(you)
		elif (client_score > 21) and ("A" in client):
			ins = client.index("A")
			client[ins] = 1
			client_score = score(client)
		print(f"\tYour cards : {you}, current score: {your_score}")
		print(f"\tComputer\'s first card: {client[0]}")
		print(f"\tYour final hand: {you}, final score: {your_score}")
		print(f"\tComputer\'s final hand:{client}, final score: {client_score}")
		if your_score > 21:
			print("You went over. You lose.")
		elif client_score > 21:
			print("You Win, The client went over.")
		elif your_score == client_score:
			print("It is a DRAW.")
		elif your_score > client_score:
			print("Client score is less, You Win.")
		else:
			print("You lose, Your score is less.")
		input()
		system("cls")
	else:
		run = False
		print("Exiting Black-Jack...")
		

		

