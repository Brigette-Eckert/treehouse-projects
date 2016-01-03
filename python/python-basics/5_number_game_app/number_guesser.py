import random

#generate a random number between 1-10
secret_num = random.randint(1,10)
print(secret_num)

while True: 
	#get number guess form player
	guess = int(input("Guess a number between 1 and 10? "))
	#compare guess to secret number
	if guess == secret_num:
		print("Congrats, you got it! My number was {}".format(secret_num))
		break
	#make sure guessed number is between 1 and 10
	elif guess > 10 or guess < 0:
		print("Please pick a number between 1 and 10")
		continue
	#print hit or miss and higher or lower
	elif guess > secret_num: 
		print("My number is lower than {}".format(guess))
		continue
	elif guess < secret_num: 
		print("My number is higher than {}".format(guess))
		continue

