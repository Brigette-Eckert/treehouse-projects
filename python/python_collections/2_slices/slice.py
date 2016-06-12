my_string = "Hello World"
print(my_string[1:5])
print(my_string)

my_list = list(range(1,6))
print(my_list[1:3])
print(my_list[0:2])
print(my_list[2:len(my_list)])
#leaving off first number starts and beginning and vice versa for last
print(my_list[:2])
print(my_list[2:])

my_new_list = [4, 2, 1, 3, 5]
my_new_list.sort()
print(my_new_list)
#using list[:] makes a copy of the list