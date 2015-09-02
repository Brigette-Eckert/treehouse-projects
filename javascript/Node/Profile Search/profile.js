var http = require("http");

// Problem: Need a simple way to look a user's badge count & js points
//Solution use Node.js to connect to Treehouse API to get profile Info to print out
//print out message
function printMess(username, badges, points) {
	var mess = username + " has " + badges + " total badge(s) & " + points + " points in JavaScript";
	console.log(mess);
}

//Print out Error Messages 
function printErr(error) {
	console.error(error.message);

};

function get(username) {
	//connect to the API URL (http://teamtreehouse.com/username.json)
	var request = http.get("http://teamtreehouse.com/" + username + ".json", function(response){ console.dir(response.statusCode);
		//Read the data
		var body = "";
		  response.on('data', function (chunk) {
	    body += chunk;
	  });
		 response.on('end', function() {
		 	if(response.statusCode === 200) {
				 	try {
				 		//Parse the data
				 	var profile = JSON.parse(body);
				 	//Print the data
				 	printMess(username, profile.badges.length, profile.points.JavaScript) 
				 	} catch(error) {
				 		//Parse Error
				 	 printErr(error);
				 }
		 	} else {
		 		//Status Code Error
		 		printErr({message: "There was an error getting the profile for " + username + ". ("+ http.STATUS_CODES[response.statusCode] +")"});
		 	}
		 });
	});

	//Connection Error
	request.on("error", printErr);	
}

module.exports.get = get;