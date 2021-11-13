# 5-3. 	Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
# 	   	variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •	 	Write an if statement to test whether the alien’s color is green. If it is, print 
# 		a message that the player just earned 5 points.
# •	 	Write one version of this program that passes the if test and another that 
# 		fails. (The version that fails will have no output.)
# 5-4. 	Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
# 		write an if-else chain.
# •	 	If the alien’s color is green, print a statement that the player just earned 
# 		5 points for shooting the alien.
# •	 	If the alien’s color isn’t green, print a statement that the player just earned 
# 		10 points.
# •	 	Write one version of this program that runs the if block and another that 
# 		runs the else block

alien_color = ['green', 'yellow', 'red']

for alien in alien_color:
	if (alien == 'green'):
		print('Player is just earned 5 points')
	else:
		print('Player is just earned 10 points')

# 5-5. 	Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# •	 	If the alien is green, print a message that the player earned 5 points.
# •	 	If the alien is yellow, print a message that the player earned 10 points.
# •	 	If the alien is red, print a message that the player earned 15 points.
# •	 	Write three versions of this program, making sure each message is printed 
# 		for the appropriate color alien.

for alien in alien_color:
	if (alien == 'green'):
		print('The player earned 5 points')
	elif (alien == 'yellow'):
		print('The player earned 10 points')
	else: 
		print('The player earned 15 points')

# 5-6.	Stages of Life: Write an if-elif-else chain that determines a person’s 
# 		stage of life. Set a value for the variable age, and then:
# •		If the person is less than 2 years old, print a message that the person is 
# 		a baby.
# •	 	If the person is at least 2 years old but less than 4, print a message that 
# 		the person is a toddler.
# •	 	If the person is at least 4 years old but less than 13, print a message that 
# 		the person is a kid.
# •	 	If the person is at least 13 years old but less than 20, print a message that 
# 		the person is a teenager.
# •	 	If the person is at least 20 years old but less than 65, print a message that 
# 		the person is an adult.
# •	 	If the person is age 65 or older, print a message that the person is an 
# 		elder.

stage_of_life = [1, 3, 9, 17, 40, 65]

for stage in stage_of_life:
	if(stage == 1):
		print('\nThe person is a baby')
	elif(stage == 3):
		print('The person is a toddler')
	elif(stage == 9):
		print('The person is a kid')
	elif(stage == 17):
		print('The person is a teenager')
	elif(stage == 40):
		print('The person is an adult')
	elif(stage >= 65):
		print('The person is elder')

# 5-7. 	Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
# 		independent if statements that check for certain fruits in your list.
# •	 	Make a list of your three favorite fruits and call it favorite_fruits.
# •	 	Write five if statements. Each should check whether a certain kind of fruit 
# 		is in your list. If the fruit is in your list, the if block should print a statement, 
# 		such as You really like bananas

favorite_fruits = ['1-р жимс', '2-р жимс', '3-р жимс']

for fruite in favorite_fruits:
	if (fruite == '1-р жимс'):
		print(f'You really like {fruite}')