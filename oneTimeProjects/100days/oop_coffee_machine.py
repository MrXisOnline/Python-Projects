from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system
from time import sleep

start_menu = Menu()
money_counter = MoneyMachine()
coffee_machine = CoffeeMaker()
run = True
while run:
	print("Welcome to Coffee-Maker")
	print("Which drink would you like?")
	drink = input(f"{start_menu.get_items()}\n")
	if drink == "resource-report":
		coffee_machine.report()
	elif drink == "money-report":
		money_counter.report()

	if drink == "exit":
		run = False
		print("Exiting...")
	elif drink not in ["resource-report", "money-report"]:
		drink_item = start_menu.find_drink(drink)
		if drink_item:
			if coffee_machine.is_resource_sufficient(drink_item):
				if money_counter.make_payment(drink_item.cost):
					coffee_machine.make_coffee(drink_item)
					sleep(5)
					system("cls")
	else:
		print("Wrong input!!!")


