my_list = [1, 2, "a", "b", "c", "d", 5, 6, 7, "f", "g", "h", 8, 9, "j"]
print(my_list[:2])
del my_list[:2]
print(my_list)
#replacing a splice
my_list[4:7] = ["e", "f"]
print(my_list)
print(my_list.index("f"))
my_list.remove("f")
print(my_list)
my_list[8:10] = "i"
print(my_list)