//problem: boring image gallery, user when clicking on image goes to a dead end
//Solution: Creat an overlay with the large image -lightbox

//$ in front just means its a reprensenation of an jQuery object
var $overlay = $('<div id="overlay"></div>');
var $image =$('<img>');
var $caption = $("<p></p>");

//an image to overlay
$overlay.append($image);

//add caption
$overlay.append($caption);


$("body").append($overlay);
  
  

$("#imageGallery a").click(function(event){
	event.preventDefault();
  var imageLocation = $(this).attr("href");
  
  //update the overlay with the image linked in the link
  $image.attr("src", imageLocation);

//show the overlay 
 $overlay.show();

 var captionText = $(this).children("img").attr("alt");
 $caption.text(captionText);
}); 

$overlay.click(function(){
	$overlay.hide();
});
