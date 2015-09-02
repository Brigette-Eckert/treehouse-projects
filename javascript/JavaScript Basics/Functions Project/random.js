
/*make function accepect upper and lower value and produce values between*/
function randomNumber (lv, hv) {
		if( isNaN(lv) || isNaN(hv) ) {
			throw new Error("Error, values must be numerical values -not strings")
	} 
		 Math.floor(Math.random() * (hv - lv + 1) + lv);
}
//call the function using different values
console.log(randomNumber(5, 25));
console.log(randomNumber(25, 200));
console.log(randomNumber(10000, 80000000 ));

//Math.floor(Math.random()*(higherLimit- lowerLimit+ 1) + lowerLimit);
console.log(randomNumber(2, "cat"))