// currently all functions are not working, unable to test

// get images (by class name)
var images = document.getElementsByClassName("image");

/* 
// get modal from html (by id)
var modal = document.getElementById("modal");

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
    // images[i].addEventListener("dblclick", openModal);
}

// variation of openModal with onclick instead of addEventListener, check if syntax is correct
// for (var i = 0; i < images.length; i++) {
//   images.onclick = function() {
//     modal.style.display = "block";
//     modalImage.src = this.src;
//   }
// }



// trying to make an event listener to select images for rerun
// trying with boolean true/false for labelling interested/not interested

var imagesAreSelected = new Array(images.length).fill(false);
var selected = new Array();

// function to select images
var selectImages = function(i) {
    if (imagesAreSelected[i] == false) {
        selected.push(images[i])
        imagesAreSelected[i] = true;
        images[i].style.border = "5px solid blue";
    } else if (imagesAreSelected[i] == true) {
        selected.pop(images[i])
        imagesAreSelected[i] = false;
        images[i].style.border = "none";
    }
}

// add event listener to every image, and ...
for (var i = 0; i < images.length; i++) {
    images[i].addEventListener("click", selectImages(i));
}


// add functionality to submit images in selected array after pressing rerun

*/
