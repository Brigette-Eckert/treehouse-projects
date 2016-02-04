'use strict'; 
//don't want a new module which is why parameters aren't inlcuded []
angular.module('todoListApp')
.controller('mainCtrl', function($scope, dataService){
    $scope.addTodo = function() {
        var todo = {name: "This is a new todo"};
        $scope.todos.unshift(todo);

    };

    dataService.getTodos(function(response){
        console.log(response.data);
        $scope.todos = response.data; 
    });

    $scope.deleteTodo = function(todo, $index) {
        dataService.deleteTodo(todo);
        $scope.todos.splice($index, 1);
    }

    $scope.saveTodos = function() {
       var filteredTodos = $scope.todos.filter(function(todo){
            if(todo.edited){
                return todo;
            };
        })
        dataService.saveTodos(filteredTodos);
    };

})
