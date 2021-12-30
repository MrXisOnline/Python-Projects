import random
import sys

def check_int(s):
	try:
		return int(s)
	except:
		return s



def main():
	game_element = ["rock", "paper", "scissor"]
	while True:
		try:
			print("0. rock")
			print("1. paper")
			print("2. scissor")
			u = check_int(input("Your Choice : "))
			if "str" in str(type(u)):
				uin = u
			else:
				try:
					uin = game_element[u]
				except Exception as e:
					print(str(e))
					print("Invalid Option")
					main()

			if uin.lower() in game_element:
				comin = random.choice(game_element)
				if uin == comin:
					print("Computer Choice :{}".format(comin))
					print("Draw")
					main()
				elif uin == "rock":
					if comin == "paper":
						print("Computer Choice :{}".format(comin))
						print("You Lose")
					elif comin == "scissor":
						print("Computer Choice :{}".format(comin))
						print("You Win")
				elif uin == "paper":
					if comin == "rock":
						print("Computer Choice :{}".format(comin))
						print("You Win")
					elif comin == "scissor":
						print("Computer Choice :{}".format(comin))
						print("You Lose")
				elif uin == "scissor":
					if comin == "rock":
						print("Computer Choice :{}".format(comin))
						print("You Lose")
					elif comin == "paper":
						print("Computer Choice :{}".format(comin))
						print("You Win")
			else:
				print("Invalid Option")
				print("Exiting Program")
				sys.exit()
		except KeyboardInterrupt:
			print("CTRL-C Detected")
			sys.exit()
		


if __name__ == '__main__':
	main()