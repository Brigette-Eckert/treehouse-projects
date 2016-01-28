//not putting empty array for depency since want it to use exisiting module- why app.js needs to be loaded first in html 
angular.module("todoListApp")
.directive("helloWorld", function(){
	//object returned is our directive 
	return {
		template: "This is the hello world directive",
		restrict: "E"
	};
	//element only restriction
});