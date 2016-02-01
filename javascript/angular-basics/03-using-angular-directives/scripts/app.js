angular.module("todoListApp", [])
    .controller('mainCtrl', function($scope){
        $scope.learningNgChange = function() {
            console.log("An input changed");
        };

        $scope.todos =[
            {"name": "pet the cat"},
            {"name": "learn more anuglar js"},
            {"name": "code"},
            {"name":"laundry"},
            {"name":"hem pants"},
            {"name":"run"}
        ]
    });

