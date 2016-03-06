'use strict';
// gets assigned to global scope normally
// but its bad code!

//var is used to restrict to a scope- even if its a global scope
badVariable = 10;

// x gets assigned to the global scope normally
// but it is bad code to initialize a variable from within
// a function without first declaring it in the global scope!
var x;

function amIGlobal() {
   x = 10;
}

//if you try and write to a non-writable object 
// fails in use strict/fails silently w/o strict mode
NaN.foobar = true;

//trying to delete an undeletable item 
// fails in use strict/fails silently w/o strict mode
delete Object.prototype;

// this is a syntax error in strict mode
// in non strict mode, the second zoo ("keepers")
// would be returned on a look up 
//keys in object should be unquine
var badObject = {
   zoo: "animals",
   internet: "trolls",
   zoo: "keepers"
}

// functions cannot have duplicate paramter names
// syntax error
function duplicateParameters(a,b,c,a) {
 debugger;
 return a + b + c
};

// Octal numbers are not allowed!
// Throws a syntax error!
var someOctal = 500 + 020;

delete cannot delete plane variables in strict mode
can only delete properties
var hahaha = "no, don't delete me!!!"
delete hahaha
