# 6-4. 	Glossary 2: Now that you know how to loop through a dictionary, clean 
# 		up the code from Exercise 6-3 (page 99) by replacing your series of print()
# 		calls with a loop that runs through the dictionary’s keys and values. When 
# 		you’re sure that your loop works, add five more Python terms to your glossary. 
# 		When you run your program again, these new words and meanings should 
# 		automatically be included in the output.

person_information = {'Овог': 'Мөнх-эрдэнэ','Нэр': 'Содсайхан', 'Нас': 22, 'Төрсөн газар': 'Мөрөн'}

for person, info in person_information.items():
	print(f'Таны {person.lower()}: {info}')

for person in person_information.keys():
	print(f"Хэрэглэгчээс авах судалгаа: {person.upper()}")

for info in person_information.values():
	print(f"Хэрэглэгчийн тухай: {info}")

# 6-5. 	Rivers: Make a dictionary containing three major rivers and the country 
# 		each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 	Use a loop to print a sentence about each river, such as The Nile runs 
# 		through Egypt.
# •	 	Use a loop to print the name of each river included in the dictionary.
# •	 	Use a loop to print the name of each country included in the dictionary.

rivers = {
	'Сэлэнгэ гол': "Сэлэнгэ аймаг",
	"Орхон гол" : "Орхон аймаг",
	"Мөрөн гол" : "Хөвсгөл аймаг"
}

for river, country in rivers.items():
	print(f'{river} {country}-т урсдаг.')

for river in rivers.keys():
	print(f'{river}')

for country in rivers.values():
	print(f'{country}')


# 6-6. 	Polling: Use the code in favorite_languages.py (page 97).
# •	 	Make a list of people who should take the favorite languages poll. Include 
# 		some names that are already in the dictionary and some that are not. 
# •	 	Loop through the list of people who should take the poll. If they have 
# 		already taken the poll, print a message thanking them for responding. 
# 		If they have not yet taken the poll, print a message inviting them to take 
# 		the poll

names = ['1-р хүн', '2-р хүн', '3-р хүн', '4-р хүн', '5-р хүн', '6-р хүн', '7-р хүн', '8-р хүн']
favorite_languages = {"1-р хүн" : "Python", "2-р хүн" : "Javascript", "3-р хүн" : "Java", "4-р хүн" : "C++", "5-р хүн" : "C"}

for favorite_language in favorite_languages.keys():
	if favorite_language in names:
		print(f'{favorite_language} thank you for responding')
	elif name not in favorite_languages:
		print(f'{favorite_language} please take a poll')