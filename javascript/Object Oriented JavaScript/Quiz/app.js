var pokeQuiz = new Quiz();
//add in questions
	var Q1 = new Question("Which pokemon were the orginal 3 starters?", "Bulbasaur, Charmander, Squirtle", [ "Turtwig, Chimchar, Piplup", "Bulbasaur, Charmander, Squirtle", "Chespin, Fennekin, Froakie"]);
	var Q2 = new Question("Who is the leader of the Elite Four in Kanto?", "Lance", ["Drasna","Drake","Lance"]);
	var Q3 = new Question("In the Anime what kind of talking Pokemon accompined Team Rocket?", "Meowth", ["Meowth", "Wobbuffet", "Cacnea"]);
	var Q4 = new Question("What is the name of Ash's orginal rival?", "Gary", ["Gary", "Douche", "Professor Oak"]);
	var Q5 = new Question("Which of the following move types is super effective against pyschic type pokemon?", "Ghost",["Pyschic", "Posion", "Ghost"]);
	var Q6 = new Question("How does vulpix 'evolve' into ninetails?", "With a fire stone", ["At level 36", "Via trade", "With a fire stone"]);
	var Q7 = new Question("What is Magikarp's final form?", "Gyarados", ["Seaking","Gyarados", "Carvanha"]);
	var Q8 = new Question("What does a Pecha Berry do?", "Cures Poison", ["Cures Poison", "Cures Confusion", "Restores 10HP"]);
	var Q9 = new Question("What item is used to wake Snorlax?", "Poké Flute", ["Poké Toy", "Poké Doll","Poké Flute"]);
	var Q10 = new Question("Which of the follow pokemon is a clone of another?", "Mewtwo", ["Mew", "Mewtwo", "Ditto"]);
	pokeQuiz.add(Q1);
	pokeQuiz.add(Q2);
	pokeQuiz.add(Q3);
	pokeQuiz.add(Q4);
	pokeQuiz.add(Q5);
	pokeQuiz.add(Q6);
	pokeQuiz.add(Q7);
	pokeQuiz.add(Q8);
	pokeQuiz.add(Q9);
	pokeQuiz.add(Q10);


//intinal footer display 
$(document).ready(function(){
var currentProgress = "Question " + (pokeQuiz.progress+1) + " of " + pokeQuiz.totalQuestions; 
document.getElementById("progress").innerHTML = currentProgress;
});

//intinal question display
var quizElement = document.getElementById("quiz");
pokeQuiz.renderInElement(quizElement);


$("#quiz").on( 'click','.btn--default',function(event) {
	if((pokeQuiz.progress+1) < pokeQuiz.totalQuestions) {
		//check if answer selected and answer are the same
		if(event.target.innerHTML === pokeQuiz.questions[pokeQuiz.progress].answer){
			pokeQuiz.score ++ 
		};
		//progress counter increase when if correct answer selected 
	 	pokeQuiz.progress ++;
	 	//display next question
	 	pokeQuiz.renderInElement(quizElement);
		var currentProgress = "Question " + (pokeQuiz.progress+1) + " of " + pokeQuiz.totalQuestions; 
		document.getElementById("progress").innerHTML = currentProgress;
	} else {
		console.log("score page!")
		pokeQuiz.results(quizElement)
		document.getElementById("progress").innerHTML=" ";
	}
});

 
