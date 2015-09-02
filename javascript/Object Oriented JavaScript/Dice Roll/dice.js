function Dice(sides) {
	this.sides = sides;
}

Dice.prototype.roll = function() {
		var randomber = Math.floor(Math.random()* this.sides) + 1;
		return randomNumber;
}

var dice6 = new Dice(6);
var dice10 = new Dice(10);

console.log(Dice.roll === dice10.roll);