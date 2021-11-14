# A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Accessing Values in a Dictionary
# === To get the value associated with a key, give the name of the dictionary and
# === then place the key inside a set of square brackets.

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x-position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
elif alien_0['speed'] == 'fast':
	x_increment = 3

alien_0['speed'] = 'fast'
alien_0['x-position'] = alien_0['x-position'] + x_increment
print(alien_0	)

# Removing Key-Value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# A Dictionary of Similar Objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}

print_value = alien_0.get('points', 'No point value assigned.')
print(print_value)

# ========================== Looping through a Dictionary ==========================  #

# Looping Through All Key-Value passed

user_0 = {
	'хэрэглэгч': 'nmwnzvl',
	'нэр': 'Намуунзул',
	'овог': 'Батмагнай',
}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

favorite_languages: {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phill': 'python',
}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

# Looping Through all the Keys in a Dictionary

favorite_languages: {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phill': 'python',
}

for name in favorite_languages.keys():
	print(name.title())

######################################################################
favorite_languages: {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phill': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}")

favorite_languages: {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phill': 'python',
}

if 'eren' not in favorite_languages.keys():
	print('Erin, please take our poll')

# Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages: {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phill': 'python',
}

for name in sorted(favorite_languages.keys()):
	print(f"\t{name.title()}, thank you for taking the poll")

# Looping Through All Values in a Dictionary

favorite_languages: {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phill': 'python',
}

print("\nThe following languages have been mentioned")
for language in favorite_languages.values():
	print(language.title())


favorite_languages: {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phill': 'python',
}

print(f"\nThe following languages have been mentioned")
for language in set(favorite_languages.values()):
	print(language.title())

# =============================== NESTING =========================== #

# List of Dictionaries

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print(...)

# Show how many aliens have been created.
print(f'Total number of aliens: {len(aliens)}')

# Make an empty list for storing aliens

aliens = []

# Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] == 'yellow'
		alien['speed'] == 'medium'
		alien['points'] == 10
# Show the first 

# A LIST in a Dictionary
pizza = {
	'crust' : 'thick',
	'toppings' : ['mushrooms', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
	'jen' : ['python', 'ruby'],
	'sarah' : ['c'],
	'edward' : ['ruby', 'go'],
	'phil' : ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

# A Dictionary in a Dictionary

users = {
	'aeinstein' : {
		'first' : 'albert',
		'last' : 'einstein',
		'location' : 'princeton',
	},
	'mcurie' : {
		'first' : 'marie',
		'last' : 'curie',
		'location' : 'paris'
	},
}

for username, user_info in users.items():
	print(f'\nUsername: {username}')
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f'\nFull name: {full_name.title()}')
	print(f'\tLocation: {location.title()}')