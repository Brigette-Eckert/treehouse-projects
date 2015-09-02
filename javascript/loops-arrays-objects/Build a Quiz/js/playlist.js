var playList = [
  ['The Walker', 'Fitz and the Tantrums'],
  ['Ohio', 'Crosy, Stills, Nash & Young'],
  ['Its My Life' , 'Bon Jovi'],
  ['Hold on Loosely', '.38 Special'],
  ['Crystals', 'Of Monsters and Men'],
  ['Shut Up and Dance', 'Walk the Moon']
];

function print(message) {
  document.write(message);
}

function printSongs( songs ) {
  var listHTML = '<ol>';
  for ( var i = 0; i < songs.length; i += 1) {
    listHTML += '<li>' + songs[i][0] + ' by ' + songs[i][1]  + '</li>';
  }
  listHTML += '</ol>';
  print(listHTML);
}

printSongs(playList);





















