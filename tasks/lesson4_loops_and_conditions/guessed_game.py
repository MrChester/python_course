import random

number = random.randint(1, 25)
guesses = 0

while guesses < 5:
	print("Enter a number from 1 to 25: ")
	guess = int(input())

	guesses += 1

	if guess != number:
		print("Did not guess!")
	else:
		print("Guessed! WIN!")
else:
	print("Guessed number is - %s" % (number))