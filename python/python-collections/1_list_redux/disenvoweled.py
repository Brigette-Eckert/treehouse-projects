#take a list of words

words = ["pirate", "lavendar", "entomology", "herbs", "cookies","feline"]
new_words = []
cased_words = []

for word in words:
	#remove all the vowels in the script
	word = list(word)
	vowels =list('aeiou')
	print("checking {}".format(''.join(word)))
	for letter in vowels: 
		while True: 
			try: 	
				word.remove(letter)
			except ValueError:
				print("{} not found".format(letter))
				break
	word[0] = word[0].upper()
	new_words.append(''.join(word))



print(new_words)



 

	#give back new words with first letter captizlied 