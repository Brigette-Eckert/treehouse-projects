var profile= require("./profile");
// using slice method when entering users on console rather than in array var users = process.argv.slice(2) 
var users =["BrigetteEckert","KennethBlack", "SamuelDurfey", "JiaoJiao"];
users.forEach(profile.get);

