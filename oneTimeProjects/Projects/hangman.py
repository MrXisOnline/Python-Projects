import random
guess = True
_guess_ = 3
words = ["dice", "hello", "player", "sun", "missisipi", "city", "values", "love", "hates"]

while guess:

	if _guess_ == 1:
		guess = False

	random_word = random.choice(words)
	print("Guess word from list", words)
	guess_word = input("Your Word :")
	if random_word == guess_word.lower():
		print("\nCorrect Guess\n")
		words.pop()
	else:
		_guess_ = _guess_ - 1
		print("Guess Remaining : %d" %_guess_)