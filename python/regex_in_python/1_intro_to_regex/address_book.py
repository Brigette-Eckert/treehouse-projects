import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# print(data)

# r stands for raw string
# match matches beginning of string- why it doesn't work for Kenneth,
# replacing with search will work anywhere in the string
last_name = r'Love'
first_name = r'Kenneth'

# print(re.match(first_name, data))
# print(re.match(last_name, data))
# print(re.search(r'Kenneth', data))

# \ is escape character- in this example \( is parenthesis instead of group
# print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))

# COUNTS
# print(re.search(r'\w+, \w+', data))
# optional parenthesis and hyphen
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# print(re.findall(r'\w*, \w+', data))

# SETS
# print(re.findall(r'[-\w\d+.]+@[-\d\w.]+', data))
# \b is word boundry
#  re.I is shorthand for re.IGNORECASE
# print(re.findall(r'\b[trehous]{9}\b', data, re.I))

# # NEGATION
# print(re.findall(r'''
#     \b@[-\w\d+.]* # Find a word boundary, an @, and then any number of characters
#     [^gov\t]+ # Ignore 1+ instances of the letters 'g', 'o', or 'v' and a tab
#     \b  # Match another word boundary
#     ''', data, re.VERBOSE | re.I))  #using verbose because of multi line string

# print(re.findall(r'''
#     \b[-\w]+, # Find a word boundary, 1+ hyphens or characters and a comma
#     \s # find 1 whitespace
#     [-\w ]+ # find 1+ hyphens and characters and explicit spaces - only match spaces not tabs or new lines
#     [^\t\n] # ignore tabs and new lines
# ''', data, re.X))  # re.X is shorthand for re.Verbose


# GROUPS
# ^ and $ stand for beginning and end of line
# line = re.search(r'''
#     ^(?P<name>[-\w]*,\s[-\w ]+)\t  # groups defined with ()
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t
#     (?P<job>[\w\s]+,\s[\w\s.]+)+\t?
#     (?P<twitter>@[\w\d]+)?$
# ''', data, re.X | re.MULTILINE)

# print(line)
# print(line.groupdict())

#Compiling and Looping with Regex
line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w]*),(?P<first>\s[-\w ]+))\t  # groups defined with ()
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t
    (?P<job>[\w\s]+,\s[\w\s.]+)+\t?
    (?P<twitter>@[\w\d]+)?$
''', re.X | re.MULTILINE)

# print(re.search(line, data).groupdict())
# print(line.search(data).groupdict())

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))
