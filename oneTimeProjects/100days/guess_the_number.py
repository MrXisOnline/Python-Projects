import random
print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 to 100.")
mode = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
attempt = None
if mode == 'easy':
	attempt = 10
elif mode == 'hard':
	attempt = 5
else:
	print("Type Carefully.")

ran_num = random.randint(1, 100)
run=True
while run:
	print(f"You have {attempt} attempts remaining to guess the number.")
	if attempt <= 0:
		print("You\'re run out of guesses, you lose.")
		run = False
		break

	guess = int(input("Make a guess: "))
	if guess > ran_num:
		print("Too high.")
		print("Guess again.")
		attempt -= 1
	elif guess < ran_num:
		print("Too Low.")
		print("Guess again.")
		attempt -= 1
	elif guess == ran_num:
		print(f"You got it! The answer was {guess}.")
		run = False