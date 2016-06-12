#for loops
my_list = ["hello", "how", "are", "you"]

for word in my_list:
	print(word)

for letter in "abcdefghijklmnopqrstuvwxyz":
	print(letter.upper())

#combinig for and conditional 
for num in [1, 2, 3, 4]:
	if num%2 == 0:
		print(num)

#while loops

start = 10
#while start is truthy 
while start:
	print(start)
	start -= 1

#break
names = ['Kenneth', 'Brigette', 'Niko', 'QUIT', 'Jenna']

for name in names:
	if name == 'QUIT':
		break
	print(name)
#continue 
#continue skips the current step
for name in names: 
	if name == "QUIT":
		continue
	print(name)

