# 9-1.  Restaurant: Make a class called Restaurant. The __init__() method for 
#       Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#       Make a method called describe_restaurant() that prints these two pieces of 
#       information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#       Make an instance called restaurant from your class. Print the two attributes individually, 
#       and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_method(self):
        print(f"{self.restaurant_name} 🍽 {self.cuisine_type} 🍴")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} open at 8 am.")

restaurant_1 = Restaurant('Restaurant 1', 'хэн мэдэх вэ?')
restaurant_2 = Restaurant('Restaurant 2', 'хэн мэдэх вэ?')

print(restaurant_1)
print(restaurant_2)
# 9-2.  Three Restaurants: Start with your class from Exercise 9-1. Create three 
#       different instances from the class, and call describe_restaurant() for each 
#       instance.

restaurant_a = Restaurant('Restaurant A', 'хэн мэдэх вэ?')
print(restaurant_a)
restaurant_a.describe_method()

restaurant_b = Restaurant('Restaurant B', 'хэн мэдэх вэ?')
print(restaurant_b)
restaurant_b.describe_method()

restaurant_c = Restaurant('Restaurant C', 'хэн мэдэх вэ?')
print(restaurant_c)
restaurant_c.describe_method()
# 9-3.  Users: Make a class called User. Create two attributes called first_name
#       and last_name, and then create several other attributes that are typically stored 
#       in a user profile. Make a method called describe_user() that prints a summary 
#       of the user’s information. Make another method called greet_user() that prints 
#       a personalized greeting to the user.
#       Create several instances representing different users, and call both methods 
#       for each user.