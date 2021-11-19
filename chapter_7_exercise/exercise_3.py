# 7-8.   Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
#        Then make an empty list called finished_sandwiches. Loop 
#        through the list of sandwich orders and print a message for each order, such 
#        as I made your tuna sandwich. As each sandwich is made, move it to the list 
#        of finished sandwiches. After all the sandwiches have been made, print a 
#        message listing each sandwich that was made.

sandwich_orders = ['1-р сандвич', "2-р сандвич", "3-р сандвич", "4-р сандвич", "5-р сандвич"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Finished sandwich: {sandwich}")
    finished_sandwiches.append(sandwich)

    # Display all confirmed users.
    print("\nThe following sandwiches are finished: ")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich)


# 7-9.   No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
#        the sandwich 'pastrami' appears in the list at least three times. Add code 
#        near the beginning of your program to print a message saying the deli has 
#        run out of pastrami, and then use a while loop to remove all occurrences of 
#        'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
#        in finished_sandwiches.

sandwich_orders = ['1-р сандвич','pastrami', "2-р сандвич", "3-р сандвич",'pastrami', "4-р сандвич",'pastrami', "5-р сандвич",'pastrami']
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# 7-10.  Dream Vacation: Write a program that polls users about their dream vacation. 
#        Write a prompt similar to If you could visit one place in the world, where 
#        would you go? Include a block of code that prints the results of the poll

# vacations = {}

# polling_active = True

# while polling_active:
#     user = input('If you could visit one place in the world, where would you go?')
#     repeat = input('Would you like to let another person respond? (yes/no)')
#     if repeat == 'no':
#         polling_acitve = False

# print("\n--- Poll results ---")
# for user in vacations:
#     print(user)