my_alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
count = 0
for letter in my_alphabet_list: 
	print('{}: {}'.format(count, letter))
	count +=1


#doing the same thing using enumerate
#gives index and value of thing at index - as a series of tuples
#can slice tuples just like lists 

for index, letter in enumerate(my_alphabet_list):
	print('{}: {}'.format(index, letter))


for step in enumerate(my_alphabet_list):
	print('{}: {}'.format(step[0], step[1]))

#singular star takes apart tuples or lists. Two stars take apart lists 

for step in enumerate(my_alphabet_list):
	print('{}: {}'.format(*step))


my_dict = {'name': 'Brigette', 'job': 'Records Specialist', 
'Employer': 'Law Firm'}

for key, value in my_dict.items():
	print('{}: {}'.format(key.title(), value))