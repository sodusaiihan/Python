# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# $$$ The keyword with closes the file once access to it is no longer needed. $$$ #

with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())

"""
Recall that Python's rstrip() method removes, or strips, any whitespace
characters from the right side of string.
"""
# -------------------- Reading Line by Line -------------------- #
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# -------------------- Making a List of Lines from a File -------------------- #

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


# -------------------- Working with a File's contents -------------------- #

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# -------------------- Large Files: One Million Digits -------------------- #