# def count_words(filename):
#     """Count the approximate number of words in a file"""
#     try:
#         with open(filename, 'r', encoding='utf-8') as f:
#             content = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the {filename} does not exist.")
#     else:
#         words = content.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")

# filenames = ["alice.txt", "Tarzan_of_the_apes.txt", "Gulliver's_Travels.txt"]
# for filename in filenames:
#     count_words(filename)

def count_words(filename):
    """Count the approximate number of words in file"""
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'Tarzan_of_the_apes.txt', "Gulliver's_Travels.txt", 'Naruto']
for filename in filenames:
    count_words(filename)