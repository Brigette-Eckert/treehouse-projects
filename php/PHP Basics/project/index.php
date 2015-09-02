<?php
  $name = "Brigette";
  $location = "Portland, OR (screw Florida!)";
  $full_name = "Brigette Eckert";
  $name = $full_name;
 ?>

<!DOCTYPE html>
<html>
  <head>
  	<meta charset=utf-8>
  	<title> <?php echo $name ?> | Treehouse Profile</title>
  	<link href="css/style.css" rel="stylesheet" />
  </head>
  
  <body>
    <section class="sidebar text-center">
      <div class="avatar">
        <img src="img/profile.jpeg" alt="<?php echo $name ?>">
      </div>
      <h1><?php echo $name ?></h1>
      <p><?php echo $location ?></p>
      <hr />
      <p>Welcome to PHP Basics!</p>
      <hr />
      <ul class="social">
        <li><a href=""><span class="icon twitter"></span></a></li>
      </ul>
    </section>
    <section class="main">
      <pre><?php 
          $greeting = "Hello, World\n";
          $greeting{0} = "J";
          $secondary_greeting = "Meow!";


          $bool = TRUE;
          //var_dump($bool);
          $bool = FALSE;
          //var_dump($bool);

          var_dump((bool)"");
          var_dump((bool)0);
          var_dump((bool)0.00);
          var_dump((bool)array());
          ?></pre>
    </section>
  </body>
</html>