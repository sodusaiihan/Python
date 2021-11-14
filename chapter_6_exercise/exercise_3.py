# 6-7.  People: Start with the program you wrote for Exercise 6-1 (page 99). 
#       Make two new dictionaries representing different people, and store all three 
#       dictionaries in a list called people. Loop through your list of people. As you 
#       loop through the list, print everything you know about each person.

people = {
    "Намуунзул" : {
        "Овог" : "Батмагнай",
        "Нэр" : "Намуунзул",
        "Нас" : "21",
    },
    "Содсайхан" : {
        "Овог" : "Мөнх-эрдэнэ",
        "Нэр" : "Содсайхан",
        "Нас" : "22",
    }
}

for username, user_info in people.items():
    print(f"Нэр: {username}")
    full_name = f"{user_info['Овог']} {user_info['Нэр']}"
    age = f"{user_info['Нас']}"

    print(f"\tОвог, Нэр: {full_name}")
    print(f'\tНас: {age}')

# 6-8.   Pets: Make several dictionaries, where each dictionary represents a different pet.
#        In each dictionary, include the kind of animal and the owner’s name. 
#        Store these dictionaries in a list called pets. Next, loop through your list and as 
#        you do, print everything you know about each pet.

нохой = {'эзэн' : 'содсайхан', 'амьтан' : 'нохой'}
муур = {'эзэн' : 'намуунзул', 'амьтан' : 'муур'}

pets = [нохой, муур]

for pet in pets:
    print(f"{pet['эзэн'].title()} {pet['амьтан']}д дуртай 🤞")

# 6-9.  Favorite Places: Make a dictionary called favorite_places. Think of three 
#       names to use as keys in the dictionary, and store one to three favorite places 
#       for each person. To make this exercise a bit more interesting, ask some friends 
#       to name a few of their favorite places. Loop through the dictionary, and print 
#       each person’s name and their favorite places.

favorite_places = {
    'Содсайхан' : {
        'газар' : 'Хөвсгөл'
    },
    'Намуунзул' : {
        'газар' : 'Увс'
    }
}

for name, place in favorite_places.items():
    print(f"\n{name.title()} {place['газар']} аймагт очих дуртай. 🌏")


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) 
#       so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
#       keys in your dictionary. Create a dictionary of information about each city and 
#       include the country that the city is in, its approximate population, and one fact 
#       about that city. The keys for each city’s dictionary should be something like 
#       country, population, and fact. Print the name of each city and all of the information you have stored about it.
# 6-12. Extensions: We’re now working with examples that are complex enough 
#       that they can be extended in any number of ways. Use one of the example programs 
#       from this chapter, and extend it by adding new keys and values, 
#       changing the context of the program or improving the formatting of the output