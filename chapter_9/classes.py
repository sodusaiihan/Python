# ******************************** CREATING THE DOG CLASS ******************************** #
# class Dog:
#     """A simple attempt to model a dog."""
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over")

# my_dog = Dog('Банхар', 28)
# my_dog.sit()
# my_dog.roll_over()

# print(f"Миний нохойг {my_dog.name} гэдэг.")
# print(f"Миний нохой {my_dog.age} настай.")

# ******************************** CREATING MULTIPLE INSTANCES ******************************** #

class Dog:
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a rolling over in response to a command."""
        print(f"{self.name} rolled over")

төвийн_нохой = Dog('Банхар', 28)
хөдөөгийн_нохой = Dog('Панда', 14)

print(f"Миний төвийн нохойны нэрийг {төвийн_нохой.name}.")
print(f"Миний төвд байдаг нохой {төвийн_нохой.age} настай.")
төвийн_нохой.sit()

print(f"Миний хөдөө байдаг нохойны нэрийг {хөдөөгийн_нохой.name}.")
print(f"Миний хөдөө байдаг нохой {хөдөөгийн_нохой.age} настай.")
хөдөөгийн_нохой.roll_over()