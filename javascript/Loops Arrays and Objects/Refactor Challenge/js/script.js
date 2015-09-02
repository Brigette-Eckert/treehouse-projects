function color() {
	return Math.floor(Math.random() * 256 ); 
}

var html = '';
var rgbColor;


for (var i=1; i<=10;i++) {
	rgbColor = 'rgb(' + color() + ',' + color() + ',' + color() + ')';
	html += '<div style="background-color:' + rgbColor + '"></div>';

}

document.write(html);