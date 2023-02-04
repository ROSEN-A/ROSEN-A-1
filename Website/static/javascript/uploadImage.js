//selecting all required elements
const photoDropArea = document.querySelector(".drag-area-photo"),
dragText = photoDropArea.querySelector("header"),
photoButton = photoDropArea.querySelector("button"),
photoInput = photoDropArea.querySelector("input");
let file; //this is a global variable and we'll use it inside multiple functions

photoButton.onclick = ()=>{
        photoInput.click(); //if user click on the button then the input also clicked
}


var imageUploaded = false;

photoInput.addEventListener("change", function(){
        //getting user select file and [0] this means if user select multiple files then we'll select only the first one
        file = this.files[0];
        photoDropArea.classList.add("active");
        showFile(); //calling function
});

