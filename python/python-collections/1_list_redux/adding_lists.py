a_list = [1, 2, 3]
#append adds list within list
a_list.append([4,5])
print(a_list)
#range will count from 0 up to but not including #
our_list = list(range(10))
print(our_list)

print(our_list + [10, 11, 12])
print(our_list)
our_list += [10, 11, 12]
print(our_list)

list_1 = ["cat", "treat", "plant"]
list_2 =["leash", "snow", "kindle"]
list_3 = list_1 + list_2
print(list_3)