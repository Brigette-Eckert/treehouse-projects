function Question(question, answer, choices) {
 	this.question = question;
 	this.answer = answer;
 	this.choices = choices;
 };
 
Question.prototype.toHTML = function() {
 	var htmlString='<h1> Poké Quiz </h1>';
 	htmlString +=  '<h2 id="question" class="headline-secondary--grouped">' + this.question  + '</h2>';
 	htmlString += '<button id="guess0" class="btn--default">';
    htmlString += this.choices[0]; 
	htmlString += '</button>';
	htmlString += '<button id="guess0" class="btn--default">';
    htmlString += this.choices[1];
    htmlString += '</button>';
	htmlString += '<button id="guess0" class="btn--default">';
    htmlString += this.choices[2]; 
	htmlString += '</button>';

        return htmlString;
    };







 
