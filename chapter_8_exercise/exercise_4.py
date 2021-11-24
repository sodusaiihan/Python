# 8-9.  Messages: Make a list containing a series of short text messages. Pass the 
#       list to a function called show_messages(), which prints each text message.

def greet_user(messages):
    for message in messages:
        print(f"{message}.")

greet = ['Таны юу санасан есөн цагаан хүсэл тань биелэх болтухай. 🌠', "Оройлсон мэдлэг өндөр байг. ✒", "Азын их тэнгэр ивээж байг."]
greet_user(greet)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
#       Write a function called send_messages() that prints each text message and 
#       moves each message to a new list called sent_messages as it’s printed. After 
#       calling the function, print both of your lists to make sure the messages were 
#       moved correctly.

def send_messages():
    greet_user(greet[:])

greet_user(greet)
send_messages()


# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the 
#       function send_messages() with a copy of the list of messages. After calling the 
#       function, print both of your lists to show that the original list has retained its 
#       messages.
