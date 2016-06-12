my_dict = {"name": "Brigette", "job": "file clerk"}
print(my_dict)

del my_dict['job']
print(my_dict)
#for changing or adding one key at a time
my_dict['age'] = 27
print(my_dict)

my_dict.update({"job": "file clerk", "breakfast": "smoothie", "name" : "BB"
	})

print(my_dict)