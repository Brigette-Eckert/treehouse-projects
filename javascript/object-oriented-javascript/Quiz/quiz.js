function Quiz() {
	this.questions = [];
	this.progress = 0; 
	this.score = 0;
	this.totalQuestions = 0;
	};

Quiz.prototype.add = function(q) {
		this.questions.push(q);
		this.totalQuestions ++;
	};
//display quiz quesstions on page
 Quiz.prototype.renderInElement = function(element) {
	element.innerHTML = "";
	element.innerHTML += this.questions[this.progress].toHTML();
};


Quiz.prototype.results = function(element) {
var results = '<h1> Results </h2>'
    results +=  '<h2> You scored ';
    results += this.score; 
    results += ' out of '
    results += this.totalQuestions;
    results += '</h2>'
   	element.innerHTML = results;
};
