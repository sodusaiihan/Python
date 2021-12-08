# 10-3. Guest: Write a program that prompts the user for their name. When they 
#       respond, write their name to a file called guest.txt.

# filename = 'User.txt'

# username = input('Та нэрээ бичнэ үү: \n')
# save_file = open(filename, 'a', encoding='utf-8')
# save_file.write(username)
    

# 10-4. Guest Book: Write a while loop that prompts users for their name. When 
#       they enter their name, print a greeting to the screen and add a line recording 
#       their visit in a file called guest_book.txt. Make sure each entry appears on a 
#       new line in the file.

# with open('guest_book.txt', 'a', encoding="utf-8") as guest:
#     accept_more_visitors = True
#     while accept_more_visitors:
#         user = input("Та нэрээ хэлнэ үү. Хэрэв та болсон гэж үзэж байгаа бол 'гарах' гэж бичнэ үү: ")
#         if user == 'гарах':
#             break
#         else:
#             guest.write(f'Таны юу санасан есөн цагаан хүсэл тань биелэх болтухай {user}\n')

# 10-5. Programming Poll: Write a while loop that asks people why they like 
#       programming. Each time someone enters a reason, add their reason to a file 
#       that stores all the responses
file_name = 'poll.txt'

with open(file_name, 'a', encoding="utf-8") as poll:
    accept_more_poll = True
    while accept_more_poll:
        polling_message = input("Та яагаад мэдээлэл технологийн салбарт орсон бэ? мөн та хүссэн үедээ гарах 🚪 гэж бичэн программыг зогсоох боломжтой:")
        if polling_message == "гарах":
            break
        else:
            poll.write(f'{polling_message}. 🥰 Маш сонирхолтой түүх байна\n')