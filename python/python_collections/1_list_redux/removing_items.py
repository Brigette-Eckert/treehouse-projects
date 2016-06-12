a_list = list("abzcd")

print(a_list.index("z"))
del a_list[2]

print(a_list)

a_string = "Hello"
del a_string
#print(a_string)
a_num = 5
del a_num
#print(a_num)


# a_string2 = "Helllo"
# del a_string2[2]
# print(a_string2)
#Doesn't work because strings are immutable 

my_list = [1, 2, 3, 1]
my_list.remove(1)
#remove removes the first incident of var in a list
print(my_list)

my_list.remove(1)
print(my_list)