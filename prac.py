print("hello, world!")


# numb_of_bread = int(input("How many pieces of bread would you like to transform into toast?"))

# def make_toast(numb_of_bread):
# 	return print("CONGRATZ! You now have {} pieces of toast. Lucky you!".format(numb_of_bread))

# your_toast = make_toast(numb_of_bread)

# modules required to do what I want.
import random


def dice_program(options):
	roll_choice = input("Would you like to roll the die? {}".format(options['delimiter']))
	
	if roll_choice == "yes":
		total = 0
		sides = int(input("How many sides? {}".format(options['delimiter'])))
		rolls = int(input("How many rolls? {}".format(options['delimiter'])))
		for i in range(rolls):
			result = roll_die(sides)
			total += result
			print_result(result)

		print("Total: {}".format(total))
		# Recursion! (**whispers** To call a function inside of itself... **fades away into the wind**)
		dice_program(options)
	else:
		print("Okay see you next time!")


def roll_die(sides):
	return random.randint(1,sides)


def print_result(result):
	return print("You rolled " + str(result))

# Recursive program 'loop'
options = {"delimiter": "\n> "}
dice_program(options)


# Program loop
# is_finished = False

# while not is_finished:
# 	is_finished = dice_program()
	