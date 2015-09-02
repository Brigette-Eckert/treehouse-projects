alert("Welcome to Javascript powered madlibs! Please follow the prompts to enter different types of words.  When you are finished, the program will fill in the blanks in the story with your choices and show you the result. Have fun!");

var questions = 10;
var questionsLeft= ' [' + questions + ' questionsLeft]'
var noun1 = prompt("nouns" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var adj1 = prompt("adjective" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var noun2 = prompt("noun" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var noun3 = prompt("nouns" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var noun4 = prompt("noun" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var noun5 = prompt("noun" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var noun6 = prompt("type of tool" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var noun7 = prompt("nouns" + ".  almost there!" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var noun8 = prompt("noun" + questionsLeft);
questions -= 1;
var questionsLeft= ' [' + questions + ' questionsLeft]';
var adj2 = prompt("adjective" + " you did it" + questionsLeft);

var story = "Planting a garden is not only fun, it also helps save";
story += " " + noun1.toLowerCase(); 
story +=". You will need a piece of";
story += " " + adj1.toLowerCase(); 
story += " " + "land. You may need a";
story += " " + noun2.toLowerCase();
story += " " + "to keep the";
story += " " + noun3.toLowerCase();
story += " " + "and" + " " + noun4.toLowerCase();
story += " " + "out. As soon as"; 
story += " " + noun5.toLowerCase();
story += " " + "is here you can go out there with your";
story += " " + noun6.toLowerCase();
story += " " + "and plant all kinds of";
story += " " + noun7.toLowerCase(); 
story += " " + "Then in a few months, you will have corn on the";
story += " " + noun8.toLowerCase();
story += " " + "and big,";
story += " " + adj2.toLowerCase();
story += " " + "flowers."; 


document.write(story);
