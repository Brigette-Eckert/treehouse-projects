/* Random Number guessing game. 
generates a number between 1 and siz and gives the player 
two chances to guess. If they first  guess is in correct, 
it will tell the player if the number is higher or lower than
their first guess. 
*/

//assume the player didn't guess correctly
var correctGuess = false;
//generate a number between 1 and 6 
var ranNum = Math.floor(Math.random() * 6) + 1;
var guess = prompt("I am thinking of a number between 1 and 6. What numbder do you think it is?");
/*if player gets first guess wrong, lets player guess again
and gives hint */j
if (parseInt(guess) === ranNum) {
	correctGuess = true;
} else if (parseInt(guess) < ranNum) {
	var guessMore = prompt("Try again. The number I am thinking of is greater than " + guess);
	if (parseInt(guessMore) === ranNum) {
		correctGuess = true;
	}
} else if (parseInt(guess) > ranNum) {
	var guessLess = prompt("Try again. The number I am thinkinf of is less than " + guess);
	if (parseInt(guessLess) === ranNum) {
		correctGuess = true;
	}

	// test if player is correct and gives correct response
}
if (correctGuess) {
	document.write("Congrats! That was the correct number! Are you pyshic?");
} else {
	document.write("Sorry. The number was " + ranNum + ". Better luck next time!");
}


