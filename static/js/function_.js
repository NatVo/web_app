window.URL = window.URL || window.webkitURL;

var fileSelect = document.getElementById("fileSelect"),
    fileElem = document.getElementById("fileElem");
    //fileOut = document.getElementById("fileOut"),


fileSelect.addEventListener("click", function (e) {
  if (fileElem) {
    fileElem.click();
  }
  e.preventDefault(); // prevent navigation to "#"
}, false);

function load_img(files) {
  if (!files.length) {

  } 

  else {
    /*
    for (var i = 0; i < files.length; i++) {
      var li = document.createElement("li");
      list.appendChild(li);
    */
    console.log('files = ', files[0]);

    var img = document.createElement('img');
    img.src = window.URL.createObjectURL(files[0]);
    console.log('\nimg_src = ', img.src);
    console.log('\nimg = ', img);

    img.onload = function() {
        fill_canvas(img);
    }
    
    //img.height = 60;

  }
}

function fill_canvas(img) {

  var canvas = document.getElementById("canvas");

  //var t_img = document.getElementById("test_img");
  //t_img.src = window.URL.createObjectURL(files[0]);

  var ctx = canvas.getContext('2d');
  //var img = new Image();

  ctx.drawImage(img, 0, 0, 100, 100);
}
