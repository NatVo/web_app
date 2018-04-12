

$(document).ready(function(){

	var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

	
	var canvas = $('#canvas')[0];
	var ctx = canvas.getContext('2d');
	var img = new Image();


	img.src = '../static/img/4.jpg';
	//img.alt = 'alt';
	//ctx.drawImage(img, 0, 0, 100, 100);

	
	$("#add_img").click( function () {
		console.log('button click');
		$("#my_file").click();

		//var myCanvas = document.getElementById('testcanvas');
		//var ctx = myCanvas.getContext('2d');
		//var img = new Image();
  
	});

    $('#my_file').change(function (e) {

        var file = e.target.files[0],
            imageType = /image.*/;


        var $image = $('<img>', { src: e.target.result });
        console.log($image);
        //img.src = '../static/img/4.jpg';
        //var canvas = $('#canvas')[0];
        //var ctx = canvas.getContext('2d');

        ctx.drawImage(img, 0, 0, 100, 100);

    });

	/*

	$('#my_file').change(function (e) {

		img.src = '../static/img/4.jpg';
		img.alt = 'alt';

	  	ctx.drawImage(img, 0, 0, 100, 100); 

	});

	*/


	/*
	document.getElementById('add_img').onclick = function() {
    	document.getElementById('my_file').click();
	};
	*/

	socket.on('connect', function() {
		console.log('connected');
	       socket.emit('my event', 'connected');
	   });

});

