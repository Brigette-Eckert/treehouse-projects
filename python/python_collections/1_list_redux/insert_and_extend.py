#extend is faster than + with large lists and adds to end of list
our_list = list(range(13))
print(our_list)
our_list.extend(range(13,21))
print(our_list)

#insert lets you add to list at specific index 
alpha = list('acdf')
print(alpha)
alpha.insert(1, "b")
print(alpha)
alpha.insert(4, "e")
print(alpha)
