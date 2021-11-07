# ================================= ORGANIZING LIST ================================= #

# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list")
print(sorted(cars))

print("\nHere is the original list again")
print(cars)

# Printing a List in Reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\n{cars}" )

cars.reverse()
print(cars)

# Finding the Length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))