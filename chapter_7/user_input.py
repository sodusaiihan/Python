# ===================================== HOW THE INPUT() FUNCTION WORKS ===================================== #
# The input() function pauses your programm and waits for the user to enter some text. Once python recieves
# user's input, it assigns that input to a variable to make it convenient for you to work with.
# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)

# # Writing clear prompts

# name = input("Please enter your name: ")
# print(f"\nАмар байна уу?, {name}")

# prompt = 'If you tell us who you are, we can personalize the messages you see.'
# prompt += '\nWhat is your first name?'

# name = input(prompt)
# print(f'\nАмархан сайн байна уу?, {name}')

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print('\nYou are tall enough to ride')
# else:
#     print("\nYou'll be able to ride when you're little longer")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f'\nThe number {number} is even')
# else:
#     print(f"\nThe number {number} is odd.")

# ===================================== INTRODUCING WHILE LOOPS ===================================== #
# The for loop takes a collection of items and executes a block of code once for each item in the collection
# In contrast, the while loop runs as long as, or while, a certian condition is true.

# The While Loop in Action
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#============================ Letting the User Choose When to quit ============================
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\n Enter 'quit' to end the programm."

# message = ""
# while message != "quit":
#     message = input(prompt)
#     print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end a program."

# message = ""
# while message != "quit":
# 	message = input(prompt)

# 	if message != "quit":
# 		print(message)

#  ============================ Using a flag ============================
# For program that should run only as long as many conditions are true
# you can define one variable that determines whether or not the entire
# programm is active. This variable called,	a flag, acts as a signal to 
# program.

# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program."

# active = True
# while active:
# 	message = input(prompt)

# 	if message == 'quit':
# 		active = False
# 	else: 
# 		print(message)

# ============================ Using break to Exit a loop ============================ #

# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.): "

# while True:
# 	city = input(prompt)

# 	if city == 'quit':
# 		break
# 	else:
# 		print(f"I'd love to go to {city.title()}")

# ============================ Using continue a loop ============================ #

# current_number = 0
# while current_number < 10:
# 	current_number += 1
# 	if current_number % 2 == 0:
# 		continue

# 	print(current_number)

# ============================ Avoiding Infinite Loops ============================ #

# x = 1
# while x <= 5:
# 	print(x)
# 	x += 1

# ===================================== USING A WHILE LOOP WHIT LISTS AND DICTIONARIES ===================================== #

# To modify a list as you work through it, use a while loop. 
# Using while loops with lists and dictionaries allows you to collect, store, and 
# organize lots of input to examine and report on later.

# ========================== Movitng Items from One List to Another ========================== #
# Start with users that need to be verified
# and an empty list to hold confirmed users.

# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed user.

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

#     # Display all confirmed users.
#     print("\nThe following users have been confirmed: ")
#     for confirmed_user in confirmed_users:
#         print(confirmed_users)


# ========================== Removing all Instances of Specific Values from a List ========================== #

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# ========================== Filling a Dictionary with User Input ========================== #
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input('What is your name? ')
    response = input('Which mountain would you like to climb someday?')

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would you like to climb {response}")