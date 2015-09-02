//problem: It looks gross in smaller broswer widths and decieves 
//soluton: Hide the text links and swap them out with a more approriate nav

//create a select and append to #menu
var $select = $("<select></select>");
$("#menu").append($select);

//cycle over menu links
$("#menu a").each(function() {
  var $anchor = $(this);
 
  //create an option 
   var $option = $("<option></option>");  
//Deal with selected options depending on current page
  if($anchor.parent().hasClass("selected")) {
    $option.prop("selected", true);
  } 

  //option's value is the href of the link
  $option.val($anchor.attr("href"));
  //options text is the text of link
$option.text($anchor.text());
  //append option to select 
  $select.append($option);
});
  // Create Button 

  
  //Bind change lister to the select 
  $select.change(function() {
    //go to the selected location
    window.location = $select.val();
  });
  

