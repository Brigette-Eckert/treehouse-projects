 $(".btn--default").click(function() {
 	console.log("Answer Selected");
 	this.progress ++;
 	//
//progress counter increase when answer selected

//make method next that clears current html and displays next questions

 });

var currentProgress = "Question " + this.progress + " of " + this.totalQuestions; 


 document.getElementById("progress").innerHTML = currentProgress;

