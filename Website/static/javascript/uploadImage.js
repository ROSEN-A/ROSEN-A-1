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



function showFile(){
    let fileType = file.type; //getting selected file type
    let validExtensions = ["image/jpeg", "image/jpg", "image/png"]; //adding some valid image extensions in array
    if(validExtensions.includes(fileType)){ //if user selected file is an image file
            let fileReader = new FileReader(); //creating new FileReader object
            fileReader.onload = ()=>{
                    let fileURL = fileReader.result; //passing user file source in fileURL variable
                    let imgTag = `<img src="${fileURL}" alt="">`; //creating an img tag and passing user selected file source inside src attribute
                    photoDropArea.innerHTML = imgTag; //adding that created img tag inside dropArea container
            }
            fileReader.readAsDataURL(file);

    } else {
            alert("This is not an Image File!");
            photoDropArea.classList.remove("active");
            dragText.textContent = "Select Photo to Upload";
    }
}

