# ============================ IF STATEMENTS ============================ #
# Simple if statements
age = 19
if age >= 18:
	print('Та одоо сонгууль өгч болно 😎')
	print('Та сонгуулиа өгсөн үү?')

# If-else statements
age = 17
if age >= 18:
	print('Та одоо сонгууль өгч болно 😎')
	print('Та сонгуулиа өгсөн үү?')
else:
	print('\nТа сонгууль өгөх насанд хүрээгүй байна 👶')
	print('Та 18 нас хүрээд сонгууль өгөх боломжтой 👨‍🎓')


age = 12
if age < 4:
	print('Your admission cost is $0')
elif age < 18:
	print('Your admission cost is $25')
else:
	print('Your admission cost is $40')

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f'\nYour admission cost is {price}')

# Using Multiple elif Blocks

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f'\nYour admission cost is {price}')

# Omitting the else Block

age = 75
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

print(f'\nYour admission cost is {price}')

# Testing multiple conditions

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print('\nAdding mushrooms')
if 'pepperoni' in requested_toppings:
	print('Adding pepperoni')
if  'extra cheese' in requested_toppings:
	print('Adding extra cheese')

# In summary, if you want only one block of code to run, use an if-elif-else
# chain. If more than one block of code needs to run, use series of independent
# if statements.

# ============================USING IF STATEMENTS WITH LISTS ============================ #

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f"\tAdding {requested_topping}")
print("\nFinished making your pizza")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if (requested_topping == 'green peppers'):
		print("\tSorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")
print("\n Finished making your pizza")

# Checking That a List Is Not Empty

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}")
	print(f"\Finished making your pizza")
else: 
	print("Are you sure you want a plain pizza?")

# Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"\tAdding {requested_topping}")
	else: 
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza")