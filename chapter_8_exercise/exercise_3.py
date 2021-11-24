# 8-6.  City Names: Write a function called city_country() that takes in the name 
#       of a city and its country. The function should return a string formatted like this:
#       "Santiago, Chile"
#       Call your function with at least three city-country pairs, and print the 
#       values that are returned.

def city_country(city, country):
    print({country}, {city})

print('Улаанбаатар', "Монгол")
print('Москва', "Орос")
print('Астана', "Казакстан")

# 8-7.  Album: Write a function called make_album() that builds a dictionary 
#       describing a music album. The function should take in an artist name and an 
#       album title, and it should return a dictionary containing these two pieces of 
#       information. Use the function to make three dictionaries representing different 
#       albums. Print each return value to show that the dictionaries are storing the 
#       album information correctly.
#       Use None to add an optional parameter to make_album() that allows you to 
#       store the number of songs on an album. If the calling line includes a value for 
#       the number of songs, add that value to the album’s dictionary. Make at least 
#       one new function call that includes the number of songs on an album.

def make_album(artist, album, number=None):
    music_album = {'Хамтлаг': artist, 'Цомог': album}

    if number:
        music_album['дууны тоо'] = number    
    return music_album

artist = make_album("Хөсөгтөн", "Жангар", 12)
print(artist)


# 8-8.  User Albums: Start with your program from Exercise 8-7. Write a while
#       loop that allows users to enter an album’s artist and title. Once you have that 
#       information, call make_album() with the user’s input and print the dictionary 
#       that’s created. Be sure to include a quit value in the while loop

def make_album(artist, album, number):
    album_title = f"Цомгийн нэр: {album}, Хамтлаг: {artist}, Дууны тоо: {number}"
    return album_title.title()

while True:
    print("Та цомгийн нэрээ оруулна уу 🎼")
    print("Та хүссэн үедээ 'q' даран гарч болно 😀")
    album = input('Цомог: ')
    if album == 'q':
        break
    print("Та хамтлагын нэрийг оруулна уу 🎙")
    print("Та хүссэн үедээ 'q' даран гарч болно 😀")
    artist = input('Хамтлаг: ')
    if artist == 'q':
        break
    print("Та цомогт багтсан тоог оруулна уу 🔢")
    print("Та хүссэн үедээ 'q' даран гарч болно 😀")
    number = input('Дууны тоо: ')
    if number == 'q':
        break
