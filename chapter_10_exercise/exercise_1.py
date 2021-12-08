# 10-1. Learning Python: Open a blank file in your text editor and write a few 
#       lines summarizing what you’ve learned about Python so far. Start each line 
#       with the phrase In Python you can. . . . Save the file as learning_python.txt in 
#       the same directory as your exercises from this chapter. Write a program that 
#       reads the file and prints what you wrote three times. Print the contents once by 
#       reading in the entire file, once by looping over the file object, and once by storing
#       the lines in a list and then working with them outside the with block.



яруу_найраг = 'Чойном.txt'

lines = []
with open(яруу_найраг, encoding='utf-8') as шүлэг:
    lines = шүлэг.readlines()

count = 0
for line in lines:
    count += 1
    print(f'{count}: {line}'.rstrip())

# 10-2. Learning C: You can use the replace() method to replace any word in a 
#       string with a different word. Here’s a quick example showing how to replace 
#       'dog' with 'cat' in a sentence:
#       >>> message = "I really like dogs."
#       >>> message.replace('dog', 'cat')
#       'I really like cats.' 
#       Read in each line from the file you just created, learning_python.txt, and 
#       replace the word Python with the name of another language, such as C. Print 
#       each modified line to the screen

үгүй = 'Үгүй.txt'
lines = []
with open(үгүй, encoding='utf-8') as үгүй_шүлэг:
    lines = үгүй_шүлэг.readlines()

count = 0
for line in lines:
    count += 1
    replace = line.replace('үгүй', '🙊')
    print(f"{count}: {line}".rstrip())
    print(replace.rstrip())