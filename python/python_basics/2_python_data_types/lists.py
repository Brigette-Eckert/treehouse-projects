my_list = [1, 2, 3]
print ("My list is")
print(my_list)
# can only concat list with lists not with ints or strings
print(my_list + [4, 5])
print ("My list is still")
print(my_list)
my_list = (my_list + [4, 5])
print ("My list is now")
print(my_list)
my_list += [6, 7]
print ("My list is now")
print(my_list)
print(my_list * 2)
my_list = [1, 2, 3, 4, 5]
# append method
my_list.append(6)
print(my_list)
# append only takes one argument 
my_list.append([7, 8])
print(my_list)
my_list = [1, 2, 3]
# extend method
my_list.extend([4, 5, 6])
print(my_list)
# use append for single items and use extend for multiple items
list_in_list = [1, 2, 3, [4, 5, 6]]
print(list_in_list)
# remove method
list_in_list.remove([4, 5, 6])
print(list_in_list)