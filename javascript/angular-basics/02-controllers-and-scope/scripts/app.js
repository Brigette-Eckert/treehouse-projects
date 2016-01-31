angular.module("todoListApp", [])
    .controller('mainCtrl', function($scope){
        $scope.helloWorld = function() {
            console.log("Hello There! This is the Hello World Controller Function in the mainCtrl");
        };
    })

    .controller('coolCtrl', function($scope){
        $scope.whoAmI = function(){
        console.log("hello there, this is the coolCtrl fucntion");
        };
        //example of prototypical interheritance in angular- if you comment out this helloWorld it will use the other helloWorld function

        $scope.helloWorld = function(){
            console.log("This is not the main ctrl!");
        }
    })
    //sibling controlers don't have access to sibling contoller functions 
    .controller('imASiblingCtrl', function($scope){
        $scope.foobar = 1234;
        });
  