/*
$(document).ready(function () {


	
});

*/

var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
window.URL = window.URL || window.webkitURL;


$("#add_img").click( function () {
	$("#my_file").click();
	
});


function load_img(files) {

    //console.log('files = ', files[0]);

    var img = document.createElement('img');
    img.src = window.URL.createObjectURL(files[0]);
    
    //console.log('\nimg_src = ', img.src);
    //console.log('\nimg = ', img);

    img.onload = function() {
        fill_canvas(img);
    }
    
}

function fill_canvas(img) {

	var canvas = document.getElementById("canvas");
  	var ctx = canvas.getContext('2d');
  	ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

  	var base64 = canvas.toDataURL();
  	socket.emit('my img', base64);
}


socket.on('connect', function() {
	console.log('connected');
       socket.emit('my event', 'connected');
});


