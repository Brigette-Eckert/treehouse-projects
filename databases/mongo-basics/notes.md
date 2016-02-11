#Genera Notes
+ Mongo is NoSQL - Not Structured Query Language 
+ Documents in mongo are seperate records
+ Unlike SQL you don't have to enter null/ store empty data for fields that don't exist in each document 
+ can chain methods in mongo 
+ Each document is treated like JS object in the shell

# top level commands
 +  mongod - runs the process
 +  mongo  - runs the shell
 +  show dbs - shows all databases 
 + show collections - shows all collections within current db
 +  use db name - creates new database or switchs to collection if already created 
 
+ db.getCollectionNames() - shows names of collections in current db 

+ Object.keys(db.collectionname.find()[0]) - shows keys for the first item in the collection. 

+ cls - clear screen

# collection commands 
 + db.post.insert ({key: value})- add data into post collection
 + db.post.find() - list all documents in the current collection
 + load(file-path) - load data from file (ex seed.js) 
+ db.collection.find()[i] - can query for specific post
	find().limit(i) - limit number of returns 
+ db.collection.getIndexes() - see indexes 
+ db.collection.createIndex({key: 1}, {})  (1 to sort in ascending order, -1 for descending order)  key is name of object we want to index. Second set of paramters is for options. 

+ db.collection.dropIndex(index_key) - delete index
+ db.collection.findOne - returns one document from the collection

+ can add in paramters with booleans to not return ex 
db.posts.find({}, {body: false, description: false})  or can put in paramters to return e {title: true} only returns title

+ update : db.collection.update({key and value for object to update}, update paramter) 

+ .sort({key to sort by :ascending or descending)

+ .skip - useful for pagenation 

# Operators 
+ $or 
	ex db.posts.find({$or [{title: "Parenting 101"}, {title: "My Awesome Recipe"]})


# Other Notes
+ Mongo hacker not working with my verison of mongo- reinstall once I figure out what is wrong with it. (Package to make mongo look prettier/easier to read)

+ language drivers aka clients, plugins, binding or wrrapers allow you to interact more easily with Mongo

+ sharding 
 allows you to store data across multiple servers (dont need full copies on each pc like with sql)