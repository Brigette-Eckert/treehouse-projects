'use strict'; 

angular.module("todoListApp")
.service('dataService', function($http) {
    this.helloConsole = function() {
        console.log("This is the hello console service")
    };

    this.getTodos = function(callback){
       $http.get('mock/todos.json')
    .then(callback)
    };

    this.deleteTodo = function(todo) {
        console.log(todo.name + " has been deleted")
    };   

    this.saveTodos = function(todos){
        console.log(todos.length + "todos have been saved")
    };
});
