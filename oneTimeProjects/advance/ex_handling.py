try:
	a = input("num:")
	print(int(a))
except ValueError:
	print("enter only number")
except KeyboardInterrupt:
	print("CTRL-C")

