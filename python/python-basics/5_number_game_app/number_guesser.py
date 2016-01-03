import random

#generate a random number between 1-10
secret_num = random.randint(1,10)
turn = 0; 

while True: 
	if turn <= 3: 
	#catch when someone adds a non interger
		try:
				#get number guess form player
				guess = int(input("Guess a number between 1 and 10? "))
					#compare guess to secret number
		except ValueError:
			print("Please enter a whole number")
		else:
			if guess == secret_num:
				turn += 1
				print("Congrats, you got it! My number was {}".format(secret_num))
				print("It took you {} tries to correctly guess my number".format(turn))
				#Allow user to play again
				play_again = input("Would you like to play again? y/n? ")
				if play_again.lower() == "y" or play_again.lower() == "yes":
					secret_num = random.randint(1,10)
					continue
				else:
					break
				#make sure guessed number is between 1 and 10
			elif guess > 10 or guess < 0:
				print("Please pick a number between 1 and 10")
				continue
			#print hit or miss and higher or lower
			elif guess > secret_num: 
				turn += 1
				print("My number is lower than {}".format(guess))
				continue
			elif guess < secret_num: 
				turn += 1
				print("My number is higher than {}".format(guess))
				continue
		# limit the number of guesses
	else:
			print("Game over.  My number was {}".format(secret_num))
		#Allow user to play again
			play_again = input("Would you like to play again? y/n? ")
			if play_again.lower() == "y" or play_again.lower() == "yes":
				secret_num = random.randint(1,10)
				continue
			else: 
				break
		
	
		
