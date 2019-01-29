var imageIndex = 3;
showImages();

function showImages() {
  var i;
  var images = document.getElementsByClassName("myImages");
  for (i = 0; i < images.length; i++) {
    images[i].style.display = "none"; 
  }
  imageIndex++;
  if (imageIndex > images.length) {imageIndex = 1} 
  images[imageIndex-1].style.display = "block"; 
  setTimeout(showImages, 2000); 
}
