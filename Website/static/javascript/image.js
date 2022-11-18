// currently all functions are not working, unable to test

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

// variation of openModal with onclick instead of addEventListener, check if syntax is correct
// for (var i = 0; i < images.length; i++) {
//   images.onclick = function() {
//     modal.style.display = "block";
//     modalImage.src = this.src;
//   }
// }



// trying to make an event listener to select images for rerun

var imagesAreSelected = new Array(images.length).fill(false);
var selected = new Array();
