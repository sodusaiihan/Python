# 7-1.  Rental Car: Write a program that asks the user what kind of rental car they 
#       would like. Print a message about that car, such as “Let me see if I can find you 
#       a Subaru.”

# car = input('What kind of rental car would you like?')
# print(f'Let me see if I can find you {car}')

# 7-2.  Restaurant Seating: Write a program that asks the user how many people 
#       are in their dinner group. If the answer is more than eight, print a message saying
#       they’ll have to wait for a table. Otherwise, report that their table is ready.

# user_groups = input('How many people in your dinner group? ')
# user_groups = int(user_groups)

# if (user_groups >= 8):
#     print('Please take a while.')
# else:
#     print('The table is ready.')

# 7-3.  Multiples of Ten: Ask the user for a number, and then report whether the 
#       number is a multiple of 10 or not

number = input('Please enter a number: ')
number = int(number)

if (number % 10 == 0):
    print('The number is a multiple of 10')
else:
    print('The number is not multiple of 10')