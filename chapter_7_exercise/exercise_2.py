# Try It Yourself
# 7-4.  Pizza Toppings: Write a loop that prompts the user to enter a series of 
#       pizza toppings until they enter a 'quit' value. As they enter each topping, 
#       print a message saying you’ll add that topping to their pizza.

# prompt = f"\nYou can add topping to your pizza. Enter a 'quit' when you are finished: "
# while True:
#     message = input(prompt)
   
#     if message == 'quit':
#         break
#     else:
#         print(f"Your message is topping in your pizza. 🍕")




# 7-5.  Movie Tickets: A movie theater charges different ticket prices depending on 
#       a person’s age. If a person is under the age of 3, the ticket is free; if they are 
#       between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
#       $15. Write a loop in which you ask users their age, and then tell them the cost 
#       of their movie ticket

# prompt = "🎟 Та хэдэн настай вэ? "

# while True:
#     message = input(prompt)
#     if int(message) < 3:
#         print('The ticket is free')
#     elif int(message) <= 12:
#         print('The ticket is 10$')
#     elif int(message) > 12:
#         print('The ticket is 15$')
#     elif message == 'quit':
#         break  

# 7-6.  Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
#       that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value.



# 7-7.  Infinity: Write a loop that never ends, and run it. (To end the loop, press 
#       ctrl-C or close the window displaying the output.)

x = 0
while x <= 10:
    print(x)