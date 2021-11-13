# ============================ Looping through an Entire List ============================ #
magicians = ['alice', 'david', 'caroline']
for magician in magicians:
	print(magician)

# Doing More Work Within a for loop 
magicians = ['alice', 'david', 'caroline']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick 🧙‍")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing something After a for loop
magicians = ['alice', 'david', 'caroline']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick 🧙‍")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone. That was a great magic show!")

# ============================ Avoiding Indentation Errors ============================ #
# Forgetting to indent
# Forgetting to Indent Additional Lines

# ============================ Making Numerical Lists ============================ #
# Using the range function
for value in range(1, 10):
	print(value)

numbers = list(range(1, 10))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 10):
	square = value ** 2
	squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
	squares.append(value**2)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# ============================ Working with Part of List ============================ #

# Slicing a List
players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[1:4])

players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[:4])

players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[2:])

players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[-3:])

# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florance', 'eli']

print("\nHere are the first three players on the team.")
for player in players[:3]:
	print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

# ============================ Tuples ============================ #

# Python refers to values that cannot change as immutable, and an immutable list is called tuple.
dimensions = (50, 100)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple
dimensions = (50, 100)
for dimension in dimensions:
	print(dimension)

# Writing over a Tuple
dimensions = (50, 100)
print("\nOriginal dimensions")
for dimension in dimensions:
	print(dimension)

dimensions = (45, 125)
print("\nModiefied dimensions")
for dimension in dimensions:
	print(dimension)

# ============================ Styling your code ============================ #


























