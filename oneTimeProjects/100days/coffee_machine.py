from coffee_machine_data import *
from os import system

def report():
	print(f"Water: {stock['Water']}ml")
	print(f"Coffee: {stock['Coffee']}gm")
	print(f"Milk: {stock['Milk']}ml")
	print(f"Money: ${stock['Money']}")


def total_money():
	quarter = input("How many quarters?: ")
	dime = input("How many dimes?: ")
	nickel = input("How many nickels?: ")
	penny = input("How many pennies?: ")
	all_coins = [quarter,dime,nickel,penny]
	for c in all_coins:
		if c == "":
			all_coins[all_coins.index(c)] = 0
	total = int(all_coins[0])*coins["Quarter"] + int(all_coins[1])*coins["Dime"] + int(all_coins[2])*coins["Nickel"] + int(all_coins[3])*coins["Penny"]
	return round(total, 2)


system("cls")
run = True
while run:
	print(art)
	coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
	if coffee_choice == "report":
		report()
	elif coffee_choice == "espresso":
		price = coffees[0]["price"]
		got_money = total_money()
		if got_money < price:
			print("print not enough money")
			print(f"Here is your refund ${got_money}")
		else:
			if (stock['Water'] < coffees[0]['ingredients']['Water']) or (stock['Coffee'] < coffees[0]['ingredients']['Coffee']) or (stock['Milk'] < coffees[0]['ingredients']['Milk']):
				print("Not Enough Resources")
				print(f"Here is your refund ${got_money}")
			else:
				return_money = got_money - price
				stock['Money'] = stock['Money'] + price
				stock['Water'] = stock['Water'] - coffees[0]['ingredients']['Water']
				stock['Milk'] = stock['Milk'] - coffees[0]['ingredients']['Milk']
				stock['Coffee'] = stock['Coffee'] - coffees[0]['ingredients']['Coffee'] 
				print(f"Here is ${return_money} in change")
				print("Here is your espresso enjoy")
	elif coffee_choice == "latte":
		price = coffees[1]["price"]
		got_money = total_money()
		if got_money < price:
			print("print not enough money")
			print(f"Here is your refund ${got_money}")
		else:
			if (stock['Water'] < coffees[1]['ingredients']['Water']) or (stock['Coffee'] < coffees[1]['ingredients']['Coffee']) or (stock['Milk'] < coffees[1]['ingredients']['Milk']):
				print("Not Enough Resources")
				print(f"Here is your refund ${got_money}")
			else:
				return_money = got_money - price
				stock['Money'] = stock['Money'] + price
				stock['Water'] = stock['Water'] - coffees[1]['ingredients']['Water']
				stock['Milk'] = stock['Milk'] - coffees[1]['ingredients']['Milk']
				stock['Coffee'] = stock['Coffee'] - coffees[1]['ingredients']['Coffee']
				print(f"Here is ${return_money} in change")
				print("Here is your latte enjoy")
	elif coffee_choice == "cappuccino":
		price = coffees[2]["price"]
		got_money = total_money()
		if got_money < price:
			print("not enough money")
			print(f"Here is your refund ${got_money}")
		else:
			if (stock['Water'] < coffees[2]['ingredients']['Water']) or (stock['Coffee'] < coffees[2]['ingredients']['Coffee']) or (stock['Milk'] < coffees[2]['ingredients']['Milk']):
				print("Not Enough Resources")
				print(f"Here is your refund ${got_money}")
			else:
				return_money = got_money - price
				stock['Money'] = stock['Money'] + price
				stock['Water'] = stock['Water'] - coffees[2]['ingredients']['Water']
				stock['Milk'] = stock['Milk'] - coffees[2]['ingredients']['Milk']
				stock['Coffee'] = stock['Coffee'] - coffees[2]['ingredients']['Coffee']
				print(f"Here is ${return_money} in change")
				print("Here is your cappuccino enjoy")
	elif coffee_choice == "exit":
		print("Exiting Coffee-Machine")
		run = False
	else:
		print("Not Correct Option")