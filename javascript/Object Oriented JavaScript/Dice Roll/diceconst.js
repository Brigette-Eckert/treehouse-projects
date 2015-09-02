function Dice (sides) {
	this.sides = sides;
	this.roll= function() {
  	var randomNumber = Math.floor(Math.random() * this.sides) + 1;
 		return randomNumber;
	}
}
var d4 = new Dice(4);
var d6 = new Dice(6);
var d8 = new Dice (8);
var d10= new Dice(10);
var d12 = new Dice(12);
var d20 = new Dice(20);

for(var i= 0; i <6; i++) {
var stat = d6.roll() + d6.roll() + d6.roll()
console.log(stat);

};