$(document).ready(function() {
$('form').submit(function(evt) {

  //code here will run when sumbitted
  evt.preventDefault(); // prevets page from reloading when sumbitted
    // the AJAX part
    var $searchField = $('#search');
    var $submitButton = $('#submit');

    $searchField.prop("disabled", true);
    $submitButton.attr("disabled", true).val("searching.....");
    var flickerAPI = "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
    var search = $searchField.val();
    var flickrOptions = {
      tags: search,
      format: "json"
    };
    function displayPhotos(data) {
      var photoHTML = '<ul>';
      $.each(data.items,function(i,photo) {
        photoHTML += '<li class="grid-25 tablet-grid-50">';
        photoHTML += '<a href="' + photo.link + '" class="image">';
        photoHTML += '<img src="' + photo.media.m + '"></a></li>';
      }); // end each
      photoHTML += '</ul>';
      $('#photos').html(photoHTML);
      //console.log(data);
      $searchField.prop("disabled", false);
      $submitButton.prop("disabled", false).val("Search");
    }

    $.getJSON(flickerAPI, flickrOptions, displayPhotos);
  }); //end sumbit- makes it wait for sumbit to run callback
}); // end ready