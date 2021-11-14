# 6-1. 	Person: Use a dictionary to store information about a person you know. 
# 		Store their first name, last name, age, and the city in which they live. You 
# 		should have keys such as first_name, last_name, age, and city. Print each 
#		piece of information stored in your dictionary.


person_information = {'first_name': 'Содсайхан', 'last_name': 'Мөнх-эрдэнэ', 'age': 22, 'city': 'Мөрөн'}

print(person_information['first_name'])
print(person_information['last_name'])
print(person_information['age'])
print(person_information['city'])


# 6-2. 	Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
# 		Think of five names, and use them as keys in your dictionary. Think of a favorite 
# 		number for each person, and store each as a value in your dictionary. Print 
# 		each person’s name and their favorite number. For even more fun, poll a few 
# 		friends and get some actual data for your program.

favorite_numbers = {'1-р хүн': 1, "2-р хүн": 2, "3-р хүн": 3, "4-р хүн": 4, "5-р хүн": 5}
print(f"1-р хүний дуртай тоо бол {favorite_numbers['1-р хүн']}")
print(f"2-р хүний дуртай тоо бол {favorite_numbers['2-р хүн']}")
print(f"3-р хүний дуртай тоо бол {favorite_numbers['3-р хүн']}")
print(f"4-р хүний дуртай тоо бол {favorite_numbers['4-р хүн']}")
print(f"5-р хүний дуртай тоо бол {favorite_numbers['5-р хүн']}")

# 6-3. 	Glossary: A Python dictionary can be used to model an actual dictionary. 
# 		However, to avoid confusion, let’s call it a glossary.
# •	 	Think of five programming words you’ve learned about in the previous 
# 		chapters. Use these words as the keys in your glossary, and store their 
# 		meanings as values.
# •	 	Print each word and its meaning as neatly formatted output. You might 
# 		print the word followed by a colon and then its meaning, or print the word 
# 		on one line and then print its meaning indented on a second line. Use the 
# 		newline character (\n) to insert a blank line between each word-meaning 
# 		pair in your output

favorite_numbers = {'1-р хүн': 1, "2-р хүн": 2, "3-р хүн": 3, "4-р хүн": 4, "5-р хүн": 5}
print(f"\n1-р хүний дуртай тоо бол {favorite_numbers['1-р хүн']}")
print(f"\n2-р хүний дуртай тоо бол {favorite_numbers['2-р хүн']}")
print(f"\n3-р хүний дуртай тоо бол {favorite_numbers['3-р хүн']}")
print(f"\n4-р хүний дуртай тоо бол {favorite_numbers['4-р хүн']}")
print(f"\n5-р хүний дуртай тоо бол {favorite_numbers['5-р хүн']}")