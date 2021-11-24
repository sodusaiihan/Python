# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. The function should print 
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments.

# def make_shirt(size, text):
#     size = input('Та хэмжээгээ оруулна уу👕🎽👚 тоогоор: ')
#     text = input('Та бичүүлэх үгээ оруулна уу 🎯☯: ')
#     size = int(size)
#     print(f"Таны оруулсан хувцасны хэмжээ {size}. Таны бичүүлэх үг '{text}'")

# make_shirt(25, 'Эд нь хэврэг эзэн нь урт наслаг.')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.

def make_shirt(size="large", text="I LOVE PYTHON"):
        print(f"Shirt size is {size}. Text is {text}")

make_shirt(size='large')
make_shirt(size='medium')
make_shirt(size='small')

make_shirt(size='large', text = 'Эд нь хэврэг. Эзэн нь мөнх байг')
make_shirt(size='medium', text = 'Хүмүнээ аливаа зүйлд зүтгэл гаргаж байж л түүнийхээ жаргал зовлон хоёрыг нь таньдаг юм. Жаргалтай болмоор байвал зүтгэж, жаргалыг олтлоо зовдог.')
make_shirt(size='small', text = 'Эд нь хэврэг. Эзэн нь мөнх байг')


# 8-5. Cities: Write a function called describe_city() that accepts the name of 
# a city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the 
# default country.

def describe_city(city, country="Монгол"):
    print(f'{country} улсын нийслэл {city}')

describe_city('Улаанбаатар')