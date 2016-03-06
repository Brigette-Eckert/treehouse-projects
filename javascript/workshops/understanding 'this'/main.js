//this in a regular fuction 

//in this case this refers to the global context- in a browser it is the window object

function helloWorld() {
  console.log("Hello world!");
  console.log(this);
};

helloWorld();