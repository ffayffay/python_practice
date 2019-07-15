# check splitter program
# import math

# def split_check(total, number_of_people):
#     if number_of_people <= 1:
#         raise ValueError("More than 1 person is required to split check!")
#     return math.ceil(total / number_of_people)

# try:
#     total_due = float(input("What is the total? "))
#     number_of_people = int(input("How many people? "))
#     amount_due = split_check(total_due, number_of_people)
# except ValueError as err:
#     print("Oh no! That's not a valid value. Try again...")
#     print("({})".format(err))

# else:
#     print("Each person owes ${}".format(amount_due))




SERVICE_CHARGE = 2
TICKET_PRICE = 10
tickets_remaining = 100

def calculate_price(desired_ticket_amount):
	return (desired_ticket_amount * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
	print("There are {} tickets remaning".format(tickets_remaining))
	name = input("What is your name?  ")
	try:
		desired_ticket_amount = int(input("{}, how many tickets would you like to buy?  ".format(name)))
		if desired_ticket_amount > tickets_remaining:
			raise ValueError("There are only {} tickets ramaining.".format(tickets_remaining))
	except ValueError as err:
		print("Oh no, we ran into an isssue. {}. Please try again".format(err))
	else:
		ticket_order_cost = calculate_price(desired_ticket_amount)
		print("{}, your tickets will cost ${}".format(name, ticket_order_cost))
		proceed = input("Would you like to proceed? Y/N  ")
	if proceed.lower() == "y":
		print("SOLD!")
		tickets_remaining -= desired_ticket_amount
	else:
		print("Okay, thank you any way, {}".format(name))

 