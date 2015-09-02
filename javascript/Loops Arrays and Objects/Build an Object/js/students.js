function print(message) {
	var output = document.getElementById('output');
	output.innerHTML += message
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

//console.log(students);

//loop through array to print student & properties 
 var name;
 var track;
 var achievements;
 var points;
 var message = "";
for(var i=0; i < students.length; i+= 1) {
	//access each sstudent array with students[student][prop] and return all so return student[][0] return [1]} etc?
		message += "<h2>Name: " + students[i].name + "</h2>";
		message += "<p>Track: " + students[i].track + "</p>";
		message += "<p>Points: " + students[i].points + "</p>";
		message += "<p>Achievements: " + students[i].achievements + "</p>"; 
}
print(message);


