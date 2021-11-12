# 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# 		lines to the end of the program that do the following:
# •	 Print the message The first three items in the list are:. Then use a slice to 
# 	 print the first three items from that program’s list.
# •	 Print the message Three items from the middle of the list are:. Use a slice to 
# 	 print three items from the middle of the list.
# •	 Print the message The last three items in the list are:. Use a slice to print the 
# 	 last three items in the list.

book = ['Өрөг цадиг тамга', 'Өрөг тунхаг тамга', 'Хан хөвүүний цурхираан', 'Монгол Товчион Түүхийн Тайлал', 'Монгол хадтын онгон түүхийн гялбаа', 'Эх үрийн судар', 'Монгол домчийн судар', 'Өгүүлэх ухаан']
print(book[:3])

print(book[3:6])

print(book[-3:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
# 	 	(page 56). Make a copy of the list of pizzas, and call it friend_pizzas. 
# 		Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message My favorite 
# 		pizzas are:, and then use a for loop to print the first list. Print the message 
# 		My friend’s favorite pizzas are:, and then use a for loop to print the second list.
#	    Make sure each new pizza is stored in the appropriate list.

my_pizzas = ['1-р пицца', '2-р пицца', '3-р пицца']
friends_pizzas = my_pizzas[:]

my_pizzas.append('4-р пицца')
friends_pizzas.append('4-1-р пицца')

print(my_pizzas)
for pizza in my_pizzas:
	print(pizza)

print(friends_pizzas)
for pizza in friends_pizzas:
	print(pizza)

# 4-12. More Loops: All versions of foods.py in this section have avoided using 
# 		for loops when printing to save space. Choose a version of foods.py, and 
# 		write two for loops to print each list of foods