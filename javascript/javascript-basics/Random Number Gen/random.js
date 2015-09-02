alert("please pick two random numbers, with the second one being of higher value than the first");
var lowerLimit = prompt("choose your first number");
var higherLimit = prompt("choose your second number");
lowerLimit = parseInt(lowerLimit);
higherLimit = parseInt(higherLimit);
var answer = Math.floor(Math.random()*(higherLimit- lowerLimit+ 1) + lowerLimit);
alert("Your number is " + answer);

//this was a test
/*for (var i = 0; i < 100; i++) {
	var test = Math.floor(Math.random()*(2-1 +1) + 1);
	console.log(test);
}*/ 