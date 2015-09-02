$(".animsition").animsition({
	inClass: 'fade-in-right-lg',
	outClass: 'fade-out-right-lg',
	linkElement: 'header a',
	inDuration: 1000,
	ourDuration: 500 //miliseconds
});

$(".header").sticky({
	getWidthFrom: ".container",
	responsiveWidth: true
});

$(".header").on("sticky-start", function(){
	$(".description").html("We build <strong> great </strong> apps")
});

$(".header").on("sticky-end", function(){
	$(".description").html("We build apps")
});

$(".hire-us").sticky({
	topSpacing:64,
	getWidthFrom: ".container",
	responsiveWidth: true

});

$(".hire-us").on("sticky-start", function(){
$(".hire-us").append("<a href='#'> Email us </a>")
});

$(".hire-us").on("sticky-end", function(){
	$(".hire-us").html("Want us to work on your project?")
});

