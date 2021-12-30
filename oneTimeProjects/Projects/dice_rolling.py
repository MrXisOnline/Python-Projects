import random

again = True
while again:
	try:
		dice = random.randint(1,6)
		print(dice)
		aga = input("enter to play again... [CTRL-C to stop or press any key]")
		if aga == '':
			continue
		else:
			break
	except KeyboardInterrupt:
		break