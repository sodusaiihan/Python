# 5-1. 	Conditional Tests: Write a series of conditional tests. Print a statement 
# 	   	describing each test and your prediction for the results of each test. Your code 
# 	   	should look something like this:
# 	   	car = 'subaru'
#  	   	print("Is car == 'subaru'? I predict True.")
# 	   	print(car == 'subaru')
# 		print("\nIs car == 'audi'? I predict False.")
# 		print(car == 'audi')
# •	 Look closely at your results, and make sure you understand why each line 
# 	 evaluates to True or False.
	
name_1 = 'Намуунзул'
if name_1 == 'Намуунзул':
	print("Is name == 'Намуунзул'? I predict TRUE.")
else: 
	print("Is name != 'Намуунзул' ? I predict FALSE")
# •	 Create at least ten tests. Have at least five tests evaluate to True and 
# 	 another five tests evaluate to False.
# 5-2. 	More Conditional Tests: You don’t have to limit the number of tests you 
# 		create to ten. If you want to try more comparisons, write more tests and add 
# 		them to conditional_tests.py. Have at least one True and one False result for 
# 		each of the following:
# •	 Tests for equality and inequality with strings
# •	 Tests using the lower() method
# •	 	Numerical tests involving equality and inequality, greater than and 
# 		less than, greater than or equal to, and less than or equal to
# •	 Tests using the and keyword and the or keyword
# •	 Test whether an item is in a list
# •	 Test whether an item is not in a lis
number = 12
if number != 11:
	print('Таны тоо 11 биш')

name_0 = 'Намуунзул'
if name_0.lower() == 'намуунзул':
	print(f"Таны нэрийг {name_0.title()} гэдэг.")

name_2 = 'Содсайхан',
name_3 = 'Намуунзул'
