дөрвөн__хүлэг = ['Мухулай', 'Боорчи', 'Борохул', 'Чулуун']
дөрвөн__нохой = ['Зэв', 'Хубилай', 'Зэлмэ', 'Сүбээдэй']
print(дөрвөн__хүлэг)
print(дөрвөн__хүлэг[0].upper())
print(f"Чингис хааны дөрвөн хүлэгийн нэг Аруладын {дөрвөн__хүлэг[1].upper()} жанжин")

# ======================= Changing, Adding, and Removing Elements ======================= #

# Modifying Elements in a List
motocycles = ['honda', 'yamaha', 'suzuki']
motocycles[0] = 'ducati'
print(motocycles)

# Adding Elements to a List

# 1. Appending Elements to the End of a List
motocycles.append('ducati')
print(motocycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 2. Inserting Elements into a list
bicycles = ['honda', 'yamaha', 'suzuki']
bicycles.insert(0, 'ducati')
print(bicycles)


# Removing Elements from a list

# 1. Removing an Item Using the del Statement
bicycles = ['honda', 'yamaha', 'suzuki']
del bicycles[0]
print(bicycles)

# 2. Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
popped_motorcycles = motocycles.pop()
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motocycles.pop()
print(f"The last motorcycles I owned was a {last_owned.title()}.")

# 3. Popping items from any Position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycles I owned was a {first_owned.title()}.")

# If you’re unsure whether to use the del statement or the pop() method, 
# here’s a simple way to decide: when you want to delete an item from a list 
# and not use that item in any way, use the del statement; if you want to use an 
# item as you remove it, use the pop() method.

# 4. Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n\tA {too_expensive.title()} is too expensive to me.")