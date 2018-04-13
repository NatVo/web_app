window.URL = window.URL || window.webkitURL;

var fileSelect = document.getElementById("fileSelect"),
    fileElem = document.getElementById("fileElem"),
    fileList = document.getElementById("fileList");

fileSelect.addEventListener("click", function (e) {
  if (fileElem) {
    fileElem.click();
  }
  e.preventDefault(); // prevent navigation to "#"
}, false);

function load_img(files) {
  if (!files.length) {
    fileList.innerHTML = "<p>No files selected!</p>";
  } else {
    fileList.innerHTML = "";
    var list = document.createElement("ul");
    fileList.appendChild(list);
    for (var i = 0; i < files.length; i++) {
      console.log('i = ', i);
      var li = document.createElement("li");
      list.appendChild(li);
      
      var img = document.createElement("img");
      console.log('\nfiles = ', files[i]);
      img.src = window.URL.createObjectURL(files[i]);
      console.log('\nimg_src = ', img.src);
      img.height = 60;

      console.log('img = ', img)
      /*
      img.onload = function() {
        window.URL.revokeObjectURL(this.src);
      }
      */
      li.appendChild(img);
      var info = document.createElement("span");
      info.innerHTML = files[i].name + ": " + files[i].size + " bytes";
      li.appendChild(info);
    }
  }
}