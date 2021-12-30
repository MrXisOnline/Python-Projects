import sys

def check_int(s):
	try:
		return int(s)
	except:
		print("enter a valid year ex 2020")
		sys.exit()


def main():
	try:
		year = check_int(sys.argv[1])
		if year%4 == 0:
			print("It\'s a Leap Year.")
		else:
			print("Not a Leap Brah")
	except KeyboardInterrupt:
		print("CTRL-C Detected")

if __name__ == '__main__':
	main()