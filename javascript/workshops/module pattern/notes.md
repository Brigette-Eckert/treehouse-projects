* functions written in normal way are scoped globally and can clutter global namespace

* can import other global vars to use locally within the module

* export allows you to not clutter global namespace and allow other parts of the app to access it

* can't share names across modules, last one loaded with override prior names if applicable 

* real life examples - twitter bootstrap repo, polyglot.js (airbnb) repo