const videoDropArea = document.querySelector(".drag-area-video"),
videoDragText = videoDropArea.querySelector("header"),
videoButton = videoDropArea.querySelector("button"),
videoInput = videoDropArea.querySelector("input");
let videoFile; //this is a global variable and we'll use it inside multiple functions

videoButton.onclick = ()=>{
        videoInput.click(); //if user click on the button then the input also clicked
}

videoInput.addEventListener("change", function(){
        //getting user select file and [0] this means if user select multiple files then we'll select only the first one
        videoFile = this.files[0];
        videoDropArea.classList.add("active");
        showFile(); //calling function
});


//If user Drag File Over DropArea
videoDropArea.addEventListener("dragover", (event)=>{
        event.preventDefault(); //preventing from default behaviour
        videoDropArea.classList.add("active");
        dragText.textContent = "Release to Upload image";
});


//If user leave dragged File from DropArea
videoDropArea.addEventListener("dragleave", ()=>{
        videoDropArea.classList.remove("active");
        dragText.textContent = "Drag & Drop to Upload image";
});


//If user drop File on DropArea
videoDropArea.addEventListener("drop", (event)=>{
        event.preventDefault(); //preventing from default behaviour
        //getting user select file and [0] this means if user select multiple files then we'll select only the first one
        videoFile = event.dataTransfer.files[0];
        showFile(); //calling function
});


function showFile(){
        let fileType = videoFile.type; //getting selected file type
        let validExtensions = ["image/jpeg", "image/jpg", "image/png"]; //adding some valid image extensions in array
        if(validExtensions.includes(fileType)){ //if user selected file is an image file
                let fileReader = new FileReader(); //creating new FileReader object
                fileReader.onload = ()=>{
                        let fileURL = fileReader.result; //passing user file source in fileURL variable
                        let imgTag = `<img src="${fileURL}" alt="">`; //creating an img tag and passing user selected file source inside src attribute
                        videoDropArea.innerHTML = imgTag; //adding that created img tag inside dropArea container
                }
                fileReader.readAsDataURL(videoFile);
        }else{
                alert("This is not an Image File!");
                videoDropArea.classList.remove("active");
                dragText.textContent = "Drag & Drop to Upload image";
        }
}




const input = document.getElementById('file-input');
const video = document.getElementById('video');
const videoSource = document.createElement('source');

input.addEventListener('change', function() {
  const files = this.files || [];

  if (!files.length) return;
  
  const reader = new FileReader();

  reader.onload = function (e) {
    videoSource.setAttribute('src', e.target.result);
    video.appendChild(videoSource);
    video.load();
    video.play();
  };
  
  reader.onprogress = function (e) {
    console.log('progress: ', Math.round((e.loaded * 100) / e.total));
  };
  
  reader.readAsDataURL(files[0]);
});