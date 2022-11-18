// get modal from html (by id)
var modal = document.getElementById("modal");
// get images (by class name), and get modal image (by id)
var images = document.getElementsByClassName("image");
var modalImage = document.getElementById("modal-img");
// get close button (by id)
var close = document.getElementById("close");

// function to display the modal, and change the modal image to the selected image in event listener
var openModal = function() {
    modal.style.display = "block";
    modalImage.src = this.src;
}

// add event listener to every image, and show modal on double click
for (var i = 0; i < images.length; i++) {
    images[i].addEventListener("dblclick", openModal);
}




// for (var i = 0; i < images.length; i++) {
//   images.onclick = function() {
//     modal.style.display = "block";
//     modalImage.src = this.src;
//   }
// }