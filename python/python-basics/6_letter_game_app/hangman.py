import random
#make a list of words
words = ["kittens", "icy", "wizard", "angle", "fire", "ocean", "whale", "mellow", "marathon", "cloistered", "ocean", "cry", "werewolf", "medal", "arch", "electricity", "royal", "existence", "nostalgic", "wheel", "rose", "mythology", "rain", "xenophobia", "exuberant", "swift", "laugh", "unicorn", "narwhal", "button", "", "tan", "sugar", "succinct", "available", "love", "candy", "marathon", "quartz", "flapjack", "squid", "cheese", "joule", "galaxy", "jazz", "raspberry", "cat", "fox", "relationship", "species", "bug", "beetle", "space", "juice", "cookies", "autumn", "summer", "solstice", "equinox", "eclipse"]

while True:
	start = input("Press enter to start, or press Q to quit ")
	if start.lower() == "q":
		break
	#pick a random word from list
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []

	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
		#draw guessed letters, spaces and strikes
		for letter in secret_word:
			if letter in good_guesses:
				print(letter, end='')
			else:
				print('_ ' , end='')

		print('')
		print('Strikes: {}/7'.format(len(bad_guesses)))
		print('')

		#take guess	
		guess = input("Guess a letter ").lower()
		
		if len(guess) !=1:
			print("You can only guess a single letter")
			continue
		elif guess in bad_guesses or guess in good_guesses:
			print("You've already guessed that letter")
			continue
		elif not guess.isalpha():
			print("You can only guess letters")
			continue

		if guess in secret_word:
			good_guesses.append(guess)
			print("bad guesses: {}".format(bad_guesses))
			if len(good_guesses) == len(list(secret_word)):
				#print out win/lose 
				print("Congratulations! We have a winner! The word was {}".format(secret_word))
				break
		else: 
			bad_guesses.append(guess)
			print("bad guesses: {}".format(bad_guesses))

	else:
		print("Sorry, you didn't guess it. The word was {}. better luck next time".format(secret_word))
