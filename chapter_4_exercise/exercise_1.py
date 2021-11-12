# Try It Yourself
# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these 
# 	   pizza names in a list, and then use a for loop to print the name of each pizza.
# •	 Modify your for loop to print a sentence using the name of the pizza 
# 	 instead of printing just the name of the pizza. For each pizza you should 
# 	 have one line of output containing a simple statement like I like pepperoni 
#  	 pizza.
# •	 Add a line at the end of your program, outside the for loop, that states 
# 	 how much you like pizza. The output should consist of three or more lines 
# 	 about the kinds of pizza you like and then an additional sentence, such as 
# 	 I really love pizza

pizzas = ['1-р дуртай пицца', '2-р дуртай пицца', '3-р дуртай пицца']
for pizza in pizzas:
	print(pizza)
for pizza in pizzas:
	print(f"I like {pizza}")
for pizza in pizzas:
	print(f"Би {pizza}-нд дуртай")
print(f"Би үнэхээр пиццанд дургүй шүү😡\n")

# 4-2. Animals: Think of at least three different animals that have a common characteristic.
#			    Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# •	 Modify your program to print a statement about each animal, such as 
# 	 A dog would make a great pet.
# •	 Add a line at the end of your program stating what these animals have in 
#    common. You could print a sentence such as Any of these animals would 
# 	 make a great pet

animals = ['чоно', 'туулай', 'буга']
for animal in animals:
	print(animal)

for animal in animals:
	print(f"{animal.title()} бол манай Монголын билэгдэл амьтан")

for animal in animals:
	print(f"{animal.title()} бол манай Монголын Билэгдэл амьтан")
print(f"Мөн би эдгээр амьтдыг маш их бишэрдэг")