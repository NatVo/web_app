


$(document).ready(function(){
	var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
	/*
	$("#add_img").click( function () {
		console.log('button click');
		$("#my_file").click();
	});
	*/

	document.getElementById('add_img').onclick = function() {
    	document.getElementById('my_file').click();
	};


	$('input[type=file]').change(function (e) {
    	//$('#customfileupload').html($(this).val());
    	console.log($(this).val());
	});

	socket.on('connect', function() {
		console.log('connected');
        socket.emit('my event', 'connected');
    });
});


