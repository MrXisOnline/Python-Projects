import sys
import time

def check_int(s):
	try:
		return int(s)
	except:
		print("Enter Integer Only")
		sys.exit()

def main():
	f = False
	try:
		num = check_int(input("Number: "))
		a=0
		b=1
		for i in range(1,100):
			if num == a:
				f = True
				break

			c = a
			a = b
			b = b + c

		if f:
			print("it\'s a Fibonacci number")
		else:
			print("Not a Fibonacci number Bruh")
	except KeyboardInterrupt:
		sys.exit()


if __name__ == '__main__':
	main()