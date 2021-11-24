# ================================================================================== #
# In this chapter you'll also learn ways to pass information to functions. You'll learn
# how to write certain functions whose primary job is display information and other functions
# designed to process data and return a value or set of values. Finally, you'll learn to store
# functions in separate files called modules to help organize your main programm files. 
# ================================================================================== # 

# Defining a Functions

# def greet_user():
#     message = input("Амархан сайн байна уу? Таныг хэн гэдэг вэ? ")
#     print(f"Таньтай танилцахад таатай байна {message}")

# greet_user()


# Passing Information to Function


# def greet_user(username):
#     print(f"{username.title()} таньтай танилцахад таатай байна. 👋")

# greet_user('Содсайхан')

# Arguments and Parameters

# ================================================================================== #
# The variable username in the definition of greet_user() is an example of a parameter,
# a piece of information the function needs to do its job. The value 'Содсайхан' in 
# greet_user('Содсайхан') is example of argument. 
# ================================================================================== # 

# ======================================== Passing arguments ======================================== #

# Positional Arguments

# def describe_pet(animal_type, pet_name):
#     '''Display information about a pet'''
#     print(f'\nНадад {animal_type} байдаг.')
#     print(f"{animal_type}-ний минь нэрийг {pet_name.title()} гэдэг.")
# describe_pet('Нохой', 'Панда')

# Multiple function calls

# def describe_pet(animal_type, pet_name):
#     '''Display information about a pet'''
#     print(f'\nНадад {animal_type} байдаг.')
#     print(f"{animal_type}-ний минь нэрийг {pet_name.title()} гэдэг.")
# describe_pet('Нохой', 'Банхар')
# describe_pet('Нохой', 'Арслан')

# Keyword Arguments
# ================================================================================== #
# A keyword argument is a name-value pair that you pass to a function. You directly
# associate the name and the within the argument, so when you pass the argument to 
# the function, there is no confusion.
# ================================================================================== # 

# def describe_pet(animal_type, pet_name):
#     '''Display information about a pet'''
#     print(f'\nНадад {animal_type} байдаг.')
#     print(f"{animal_type}-ний минь нэрийг {pet_name.title()} гэдэг.")
# describe_pet(animal_type='Нохой', pet_name='Банхар')

# Default Values.

# def describe_pet(pet_name, animal_type="Нохой"):
#     '''Display information about a pet'''
#     print(f'\nНадад {animal_type} байдаг.')
#     print(f"{animal_type}-ний минь нэрийг {pet_name.title()} гэдэг.")
# describe_pet(pet_name='Банхар')

# *************** RETURN VALUES *************** #

# The value the function returns is called a return value. The return statement
# take a value from inside a function and sends it back to the line that called
# the function. Return values allow you to move much of your programm's grunt
# work into functions, which can simplify the body of your programm.

# def get_formatted_name(firstname, lastname):
#     '''Return a full name, neatly formatted.'''
#     full_name = f"{lastname} {firstname}"
#     return full_name.title()

# programmist = get_formatted_name('cодсайхан', 'мөнх-эрдэнэ')
# print(programmist)


# def get_formatted_name(firstname, middle_name, lastname):
#     '''Return a full name, neatly formatted.'''
#     full_name = f"Ургийн овог: {middle_name}, Овог: {lastname}, Нэр: {firstname}"
#     return full_name.title()

# programmist = get_formatted_name("Барнууд", "Мөнх-эрдэнэ", "Содсайхан")
# print(programmist)


# def get_formatted_name(firstname, lastname, middle_name=''):
#     '''Return a full name, neatly formatted.'''

#     if middle_name:
#         full_name = f"Ургийн овог: {middle_name}, Овог: {lastname}, Нэр: {firstname}"
#     else:
#         full_name = f"Овог: {lastname}, Нэр: {firstname}"
#     return full_name.title()

# programmist = get_formatted_name("Содсайхан", "Мөнх-эрдэнэ", "Барнууд")
# print(programmist)

# programmist = get_formatted_name("Содсайхан", "Мөнх-эрдэнэ")
# print(programmist)

# *************** RETURNING A DICTIONARY *************** #

# def build_person(first_name, last_name):
#     '''Return a dictionary of information about a person'''
#     person = {'Овог': last_name, 'Нэр': first_name}
#     return person

# programmist = build_person("Содсайхан", "Мөнх-эрдэнэ")
# print(programmist)

# def build_person(first_name, last_name, age = None):
#     '''Return a dictionary of information about a person'''
#     person = {'Овог': last_name, 'Нэр': first_name}
#     if age:
#         person['Нас'] = age
#     return person

# programmist = build_person("Содсайхан", "Мөнх-эрдэнэ", 22)
# print(programmist)

# *************** Using a Function with a while loop *************** #

# def get_formatted_name(lastname, firstname):
#     '''Return a full name, neatly formatted.'''
#     fullname = f"{lastname} {firstname}"
#     return fullname.title()

# # This is a infinite loop!
# active = True

# while active:
#     print('\nPlease tell me your name.')
#     f_name = input("Нэр: ")
#     f_last = input("Овог: ")

#     formatted_name = get_formatted_name(f_last, f_name)
#     print(f"Амархан сайн байна уу? {formatted_name.title()}")

# def get_formatted_name(lastname, firstname):
#     '''Return a full name, neatly formatted.'''
#     fullname = f"{lastname} {firstname}"
#     return fullname.title()

# # This is a infinite loop!
# active = True

# while active:
#     print('\nPlease tell me your name.')
#     print("enter 'q' at any time to quit")
#     f_name = input("Нэр: ")
#     if f_name == 'q':
#         break
#     f_last = input("Овог: ")
#     if f_last == 'q':
#         break
#     formatted_name = get_formatted_name(f_last, f_name)
#     print(f"Амархан сайн байна уу? {formatted_name.title()}")

# *************** Passing a List *************** #

# def greet_users(names):
#     '''Print a simple greeting to each user in the list'''
#     for name in names:
#         msg = f"{name} таны юу санасан есөн цагаан хүсэл тань биелэх болтухай."
#         print(msg)

# usernames = ["Содсайхан", "Намуунзул", "Түвдэндорж"]
# greet_users(usernames)

# *************** Modifying a List in a Function *************** #
# Start with some designs that need to be printed.
# unprinted_designs = ['phone_case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print(f"\nThe following models have been printed.")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """Show all the models that were printed """
#     print("\nThe following models have been printed")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# *************** Passing an Abritrary Number of Arguments *************** #

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# *************** Mixing Positional and Arbitrary Arguments *************** #
def make_pizza(size, *toppings):
    """ Summarize the pizza we are about to make. """
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# *************** Using Arbitrary Keyword Arguments *************** #

def build_profile(last, first, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['Овог'] = first
    user_info['Нэр'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)