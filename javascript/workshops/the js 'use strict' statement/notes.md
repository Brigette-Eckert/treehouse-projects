* use strict catches and doesn't allow errors such as not using var etc- will say undfiend rather than declaring var  (ie badVarible = 10)

* global vars clutter the main space
don't want to avoid to many global variables that might effect teammates code or 3rd party libraries/plugins

* strict mode elmites silent errors

* use strict statement has to be a string and if global first line of interrepted code 

* can use use strict within functions - useful for larger projects or if you expect a lot of other people to use the code

* when one error takes place it stops the application (first one stops so it doesn't go futher)