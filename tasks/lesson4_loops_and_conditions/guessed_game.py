import random

number = random.randint(1, 25)
guesses = 0

while guesses < 5:
	print("Enter a number from 1 to 25: ")
	guess = int(input())

	guesses += 1

	if guess < number:
		print("Too low, try again")
	if guess > number:
		print("Too high, try again")
	if guess == number:
		print("You guessed the number in %s tries" % str(guesses))
		break
else:
	print("You did not guess the number, it was %s" % str(number))