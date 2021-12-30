import os
art = '''

░█████╗░██╗░░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
███████║██║░░░██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
██╔══██║██║░░░██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
██║░░██║╚██████╔╝╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

'''
bid_list={}
run = True
while run:
	print(art)
	print("Welcome to the secret action program.")
	name = input("What is your name?: ")
	bid = int(input("Whts\'s your bid?: $"))
	bid_list[name] = bid
	cont = input("Are there any other bidders? Type \'yes\' or \'no\'.").lower()
	if cont == "yes":
		if os.name == 'nt':
			os.system("cls")
		else:
			os.system("clear")
		continue
	else:
		if os.name == 'nt':
			os.system("cls")
		else:
			os.system("clear")
		run = False

highest_bid=0
name = ""
for key in bid_list:
	if bid_list[key] > highest_bid:
		highest_bid = bid_list[key]
		name = key

print(f"The Winner is {name} with a bid of ${highest_bid}")