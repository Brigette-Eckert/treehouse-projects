/*Ask at least five questions

Keep track of the number of questions the user answered correctly

Provide a final message after the quiz letting the user know the number of questions he or she got right.

Rank the player. If the player answered all five correctly, give that player the gold crown: 3-4 is a silver crown; 1-2 correct answers is a bronze crown and 0 correct is no crown at all. */

//intial score set to zero
var score = 0;

//if loops adding point if answer was correct- no point given if incorrect

var answer1 = prompt("What is the term for a group of cats?")
	if (answer1.toLowerCase() === "clowder") {
		score += 1; 
	}

var answer2 = prompt("Who coined the term 'debugging' in programmings")
	if (answer2.toLowerCase() === "grace hopper") {
		score += 1;
	}

var answer3 = prompt("What period of artists are the Teenage Mutant Ninja Turtles Named After?")
	if (answer3.toLowerCase() === "renaissance") {
		score +=1;
	}

var answer4 = prompt("What was Elenaor Roosevelt's maiden name?")
	if (answer4.toLowerCase() === "roosevelt") {
		score +=1;
	}

var answer5 = prompt("What is the name for a brain cell?")
	if(answer5.toLowerCase() === "neuron") {
		score +=1;
	}


/*aler with number of questions answered correctly  */
alert("You answered " + score + " questions correctly");

//if else loops to letwt player know which award they won. 

//added in image for gold crown. Still need other images
	if (score === 5) {
		document.write("<p> <strong>Congratulations! You've earned a gold crown! </strong></p> <img src = 'img/gold.jpg'>")
	
} else if (score === 3 || score === 4) {
	document.write("<p> </strong> Good job! You've earned a sliver crown!</strong></p>")

}else if (score === 1 || score === 2){
	document.write("<p><strong>Nice work. You've earned a bronze crown!</strong></p>")

} else if (score === 0) {
	document.write("<p><strong>Thanks for playing! You've earned a particpation ribbon. </strong></p>")
}
 <
 