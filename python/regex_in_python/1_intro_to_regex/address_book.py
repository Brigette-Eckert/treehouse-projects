import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

print(data)

# r stands for raw string
# match matches beginning of string- why it doesn't work for Kenneth, replacing with search will work anywhere in the string
last_name = r'Love'
first_name = r'Kenneth'

print(re.match(first_name, data))
print(re.match(last_name, data))
# print(re.search(r'Kenneth', data))
