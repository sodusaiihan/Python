# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
# 		simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the 
# 	 change.
# •	 The restaurant changes its menu, replacing two of the items with different 
# 	 foods. Add a line that rewrites the tuple, and then use a for loop to print 
# 	 each of the items on the revised menu

restaurant = ("1-р хоол", "2-р хоол", "3-р хоол", "4-р хоол", "5-р хоол")
for restauran in restaurant:
	print(restauran)

restaurant = ("1.1-р хоол", "2.1-р хоол", "3-р хоол", "4-р хоол", "5-р хоол")

for restauran in restaurant:
	print(restauran)