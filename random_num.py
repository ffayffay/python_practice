
import random


def get_random_numb(n):
	return random.randint(1,n)


def run_guess_numb_game(result):
	print(result)

	try:
		guess_prompt = int(input("What is your guess?"))
	except ValueError:
		return print("Answer must be a number.")

	if guess_prompt < result:
		print("Your guess is too low.")
		run_guess_numb_game(result)

	elif guess_prompt > result:
		print("Your guess is too high.")
		run_guess_numb_game(result)

	else:
		return print("You guess correctly!! Great job!")
		

print("You have three tries to guess a number between 1 and 50!")
result = get_random_numb(50)
run_guess_numb_game('butt')



