from os import system
def calc(n1,op,n2):
	if op == "+":
		return n1+n2
	elif op == "-":
		return n1-n2
	elif op == "*":
		return n1*n2
	elif op == "/":
		return n1/n2
	else:
		return "Invalid Operation"
art = '''
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''
print(art)
run = True
num1 = int(input("What\'s the first number?: "))
print("+\n-\n*\n/")
op = input("Pick an operation: ")
num2 = int(input("What\'s the nest number?: "))
result = calc(num1,op,num2)
print(f"{num1} {op} {num2} = {result}")
again = input(f"Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ").lower()
if again == "y":
	num1 = result
	system("cls")
	pass
else:
	run = False
while run:
	print(art)
	print("+\n-\n*\n/")
	op = input("Pick an operation: ")
	num2 = int(input("What\'s the next number?: "))
	result = calc(num1,op,num2)
	print(f"{num1} {op} {num2} = {result}")
	again = input(f"Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ").lower()
	if again == "y":
		num1 = result
		system("cls")
		continue
	else:
		run = False