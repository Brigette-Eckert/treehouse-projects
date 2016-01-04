import os
import sys
import random

#make a list of words
words = ["kittens", "icy", "wizard", "angle", "fire", "ocean", "whale", "mellow", "marathon", "cloistered", "ocean", "cry", "werewolf", "medal", "arch", "electricity", "royal", "existence", "nostalgic", "wheel", "rose", "mythology", "rain", "xenophobia", "exuberant", "swift", "laugh", "unicorn", "narwhal", "button", "tan", "sugar", "succinct", "available", "love", "candy", "marathon", "quartz", "flapjack", "squid", "cheese", "joule", "galaxy", "jazz", "raspberry", "cat", "fox", "relationship", "species", "bug", "beetle", "space", "juice", "cookies", "autumn", "summer", "solstice", "equinox", "eclipse"]

#clear screen
def clear():
	if os.name == 'nt':
		os.system('cls')
	else: 
		os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
	clear()
	print('Strikes: {}/7'.format(len(bad_guesses)))
	print('')

	for letter in bad_guesses:
		print(letter, end='')
	print('\n\n')

	for letter in secret_word:
		if letter in good_guesses:
			print(letter, end='')
		else:
			print('_ ' , end='')

	print('')

def get_geuss(bad_guesses, good_guesses):
	while True:
		#take guess	
		guess = input("Guess a letter ").lower()
		
		if len(guess) !=1:
			print("You can only guess a single letter")
		elif guess in bad_guesses or guess in good_guesses:
			print("You've already guessed that letter")
		elif not guess.isalpha():
			print("You can only guess letters")
		else: 
			return guess
def play(done):
	clear()
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []

	while True:
		draw(bad_guesses, good_guesses, secret_word)
		guess = get_geuss(bad_guesses, good_guesses)

		if guess in secret_word:
			good_guesses.append(guess)
			found = True
			for letter in secret_word:
				if letter not in good_guesses:
					found = False
			if found: 
				draw(bad_guesses, good_guesses, secret_word)
				print("Congratulations! You win!")
				print("The word was {}".format(secret_word))
				done = True
		else: 
			bad_guesses.append(guess)
			if len(bad_guesses) == 7:
				draw(good_guesses, bad_guesses, secret_word)
				print("You lose.")
				print("The word was {}.".format(secret_word))
				done = True

		if done: 
			play_again = input("Play again? Y/n ").lower()
			if play_again != 'n':
				return play(done=False)
			else:
				sys.exit()

def welcome():
	start = input("Press enter to start or Q to quit ").lower()
	if start == "q":
		print("Bye!")
		sys.exit()
	else:
		return True
print("Welcome")

done = False

while True:
	clear()
	welcome()
	play(done)

#bugs: prints win message  multlipe times, says you've won after one correct guesses- the word was '.'