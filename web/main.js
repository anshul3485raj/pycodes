// set window resize limit
window.onresize = function () {
  if (
    window.outerWidth < 900 ||
    window.outerHeight < 600 ||
    window.outerWidth > 900 ||
    window.outerHeight > 600
  ) {
    window.resizeTo(1000, 600);
  }
};

var x = 0;

// get url
function generateQR() {
  var url = document.getElementById("input").value;
  eel.qrcode_generator(url)(setImage);
  if (x % 2 == 0) {
    console.log("Not reloaded !");
  } else if (x % 2 != 0) {
    location.reload();
  }
  x += 1;
}

// set image to div
function setImage() {
  var div = document.getElementById("qr_image");
  var img1 = document.createElement("IMG");
  img1.setAttribute("id", "qr");
  img1.src = "myqr.png";
  div.append(img1);
}
