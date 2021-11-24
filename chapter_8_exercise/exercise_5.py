# 8-12. Sandwiches: Write a function that accepts a list of items a person wants 
#       on a sandwich. The function should have one parameter that collects as many 
#       items as the function call provides, and it should print a summary of the
#       sandwich that’s being ordered. Call the function three times, 
#       using a different number of arguments each time.

def make_sandwich(*sandwiches):
    print(f"------------------------------------------")
    print(sandwiches)

make_sandwich('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a 
#       profile of yourself by calling build_profile(), using your first and last names 
#       and three other key-value pairs that describe you.

# def build_profile(овог, нэр, **хэрэглэгчийн_мэдээлэл):
#     """Build a dictionary containing everything we know about a user."""
#     хэрэглэгчийн_мэдээлэл['Овог: '] = овог
#     хэрэглэгчийн_мэдээлэл['Нэр: '] = нэр
#     return хэрэглэгчийн_мэдээлэл

# хэрэглэгч = build_profile(овог="Мөнх-эрдэнэ", нэр="Содсайхан", хүйс="эр", нас=22, мэргэжил="программист")

# build_profile(хэрэглэгч)

# 8-14. Cars: Write a function that stores information about a car in a dictionary. 
#       The function should always receive a manufacturer and a model name. It 
#       should then accept an arbitrary number of keyword arguments. 
#       Call the function with the required information and two other name-value pairs, such as a 
#       color or an optional feature. Your function should work for a call like this one:
#       car = make_car('subaru', 'outback', color='blue', tow_package=True)
#       Print the dictionary that’s returned to make sure all the information was 
#       stored correctly.

# def car_information(manufactur: str, model: str, **description):
#     description['Үйлдвэрлэсэн газар: '] = manufactur,
#     description['Загвар'] = model,
#     return description

# car = car_information('Монгол', 'Хулан', өнгө='бор')
# car_information(car)

def build_profile(manufactur, model, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['Үйлдвэрлэсэн газар'] = manufactur
    user_info['Загвар'] = model
    return user_info

user_profile = build_profile('Монгол', 'Хулан-1', өнгө='бор', хурд='200km')
print(user_profile)