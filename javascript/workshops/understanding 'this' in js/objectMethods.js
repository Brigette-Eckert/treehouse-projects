//this within a method on an object 

var Portland = {
    bridges: 12,
    airport: 1,
    soccerTeams: 1,
    logNumberOfBridges: function() {
        console.log("There are " + this.bridges + " bridges in Portland!")
    }
}

function logTeams () {
      console.log(this);
    }

Portland.foo = logTeams;

Portland.foo();
logTeams();

//this is the module context (node global object) and doesn't have a key on it-why it comes up undefined 