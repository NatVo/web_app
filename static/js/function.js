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

  	return canvas.toDataURL();

}


socket.on('responce', function(responce, flag) {
	//console.log(responce);

	if (flag) {
		$('#message').html('<p style = "color:green;">' + responce + '</p>')
	}
	else {
		$('#message').html('<p style = "color:red;">' + responce + '</p>');
	}
    
});




$("#sign_in").click( function () {

	if ($('#login').val().length > 0 && $('#password').val().length > 0) {

		var canvas = document.getElementById("canvas");	
		var base64 = canvas.toDataURL();

		console.log('sign in');
	 
	    socket.emit('signin_input', 
	    				base64.split(',')[1], 
	    				$('#login').val(), 
	    				$('#password').val());

	    $('#message').html('');


	}
	else {
		$('#message').html('<p style = "color:red;"> Данные некорректны! </p>');
	}

});


$("#log_in").click( function () {

	if ($('#login').val().length > 0 && $('#password').val().length > 0) {

		var canvas = document.getElementById("canvas");	
		var base64 = canvas.toDataURL();
	 
	 	console.log('log in');

	    socket.emit('login_input', 
	    				base64.split(',')[1], 
	    				$('#login').val(), 
	    				$('#password').val());

	    $('#message').html('');


	}
	else {
		$('#message').html('<p style = "color:red;"> Данные некорректны! </p>');
	}

});



