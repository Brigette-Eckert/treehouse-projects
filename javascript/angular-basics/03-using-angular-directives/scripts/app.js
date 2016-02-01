angular.module("todoListApp", [])
    .controller('mainCtrl', function($scope){
        $scope.helloWorld = function() {
            console.log("Hello There! This is the Hello World Controller Function in the mainCtrl");
        };

        $scope.todos =[
            {"name": "pet the cat"},
            {"name": "learn more anuglar js"},
            {"name": "wake up and make money"},
            {"name":"laundry"},
            {"name":"hem pants"},
            {"name":"run"}
        ]
    });

