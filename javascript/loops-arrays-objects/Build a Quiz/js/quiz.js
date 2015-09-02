
function print(message) {
  var output = document.getElementById('output')
  output.innerHTML = message;
}

// two dimenisoinal array that holds questions and answers (3 questions total). Use prompt method to ask question
 var quiz = [ 
 ['What year did World War 1 begin?', '1914'],
 ['What was the name of the first artifical satellite launched in space?', 'Sputnik'],
 ["In the Harry Potter series, what is Professor McGonagall's first name?", 'Minerva']
];



//loop to cycle through questions
var answer; 
var correctAnswer = [];
var wrongAnswer = [];
var wrongAnswers = [];
for (i=0; i<quiz.length; i++) {
	answer = prompt(quiz[i][0])
	console.log(answer);
	if(answer.toLowerCase()===quiz[i][1].toLowerCase()) {
		correctAnswer.push(quiz[i]);
		console.log(correctAnswer)
	} else {
		wrongAnswer.push(quiz[i]);
		wrongAnswers.push(answer);
	}
}


var message = "<h2>You got <strong>" + correctAnswer.length + "</strong> questions right</h2>";
for(var i=0; i<correctAnswer.length;i++) {
	message +='<p>'+correctAnswer[i][0]+'<br>';
	message +='<strong>'+correctAnswer[i][1]+'</strong></p>';
}
message += "<h2>You got the following questions wrong</h2>";
for (var i=0; i<wrongAnswer.length; i++) {
	message +='<p>'+wrongAnswer[i][0]+'<br>';
	message +='<strong>'+wrongAnswers[i]+'</strong></p>'
}
print(message);

//print answers answered correctly and questions answered incorrectly to the webpage