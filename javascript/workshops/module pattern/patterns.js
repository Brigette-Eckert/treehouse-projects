//wrapping function foo inside of anymous function makes it so function foo is no longer on the global scope


// (function(){
//   function foo(){
//   console.log('foobar');
// };

// foo();
// }());

//replacing first closure with ! or + (before anymous function) is also valid way of writing this. Helps for concating modules
// !function(){
//   function foo(){
//   console.log('foobar');
// };

// foo();
// }();

//refrencing varible in local scope is faster than using global
// !function(underscore){
//   underscore.someawesomemethod = "yay!!!!";
//   console.log(underscore.VERSION);
// }(_);



//adding sub object
var awesomeNewModule.sub = (function(exports){ 
  var exports = {
    foo: 5,
    bar: 10
  };
  
  exports.helloMars = function() {
    console.log("Hello Mars!");
  };
  
  exports.goodbye = function() {
    console.log("Goodbye!");
  };
  
  return exports
  //if awesomeNewModule exists import it - if it doesnt , delcare it as an empty object
}(awesomeNewModule.sub || {}));