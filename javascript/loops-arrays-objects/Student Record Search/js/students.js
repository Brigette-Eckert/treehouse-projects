function print(message) {
	var output = document.getElementById('output');
	output.innerHTML += message
}
function printStudent(student) {
		var message = "<h2>Name: " + student.name + "</h2>";
		message += "<p>Track: " + student.track + "</p>";
		message += "<p>Points: " + student.points + "</p>";
		message += "<p>Achievements: " + student.achievements + "</p>"; 
		print(message);
}
//array named students with name, track, achivements (numbers ), and points at least 5 students 
var students = [
	{
		name: "Brigette",
		 track:"Front End Development", 
		 achievements: '28',
		 points: '2509'
		},

	{
		name: "Thelma", 
		track: "Design",
		achievements: '9', 
		points: '667'
	},

	{
		name: "Kenneth", 
		track: "Front End Development", 
		achievements:'50', 
		points: '4572'
	},

	{
		name: "Jihoon", 
		track: "Android", 
		achievements:'49', 
		points: '3883' 
	},

	{
		name: "Samuel", 
		track: "Front End Development", 
		achievements: "6", 
		points:"352"}
];
var name;
var track;
var achievements;
var points;
var message = "";


//create a search function for names with prompts and quit to exit loop- only show data for the searched student 

while (true) {
	var search = prompt("Enter a students name to pull up their record. Enter quit to exit the search");
	search= search.toLowerCase();
	var studentFound = false;
	if (search === null || search === "quit") {
		break;
	} else if (search === "clear") {
		document.getElementById('output').innerHTML = "";
	} else {
		for(i =0; i < students.length; i ++) {
			console.log(students[i]);
			var record=students[i];
			console.log(record.name);
			if (record.name.toLowerCase() === search) {
				printStudent(record);
				studentFound = true;
			}
		};
		if(studentFound === false) {
			print("<h2> There is no student record for " + search + "</h2>");
		} 
	}
}	

