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
var videoUploaded = false;

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

                // successful image upload
                imageUploaded = true;
                if ( videoUploaded == true ) {
                        //enable
                }

        } else {
                alert("This is not an Image File!");
                photoDropArea.classList.remove("active");
                dragText.textContent = "Select Photo to Upload";
        }
}






const videoDropArea = document.querySelector(".drag-area-video"),
videoDragText = videoDropArea.querySelector("header"),
videoButton = videoDropArea.querySelector("button"),
videoSource = document.createElement('source'),
video = document.getElementById('video'),
videoInput = videoDropArea.querySelector("input");
let videoFile; //this is a global variable and we'll use it inside multiple functions

videoButton.onclick = ()=>{
        videoInput.click(); //if user click on the button then the input also clicked
}

videoInput.addEventListener("change", function(){
        // get video file for checking type
        videoFile = this.files[0];

        document.getElementById("videoDragText").style.display = "none";
        document.getElementById("videoUpload").style.display = "none";
        document.getElementById("videoSpacing").style.display = "none";
        document.getElementById("video").style.display = "block";
        
        const files = this.files || [];

        if (!files.length) return;



        // checking if video type matches valid extensions
        let videoFileType = videoFile.type; // getting the file type of the selected video
        let validVideoExtensions = ["video/mp4"];
        if(validVideoExtensions.includes(videoFileType)) {

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

        // successful video upload
        videoUploaded = true;
        
        if ( imageUploaded == true ) {
                //enable
        }
        } else {
                alert("This is not a Video File!");
                document.getElementById("video").style.display = "none";
                document.getElementById("videoDragText").style.display = "block";
                document.getElementById("videoUpload").style.display = "block";
                document.getElementById("videoSpacing").style.display = "block";
                videoDropArea.classList.remove("active");
                videoDragText.textContent = "Select Video to Upload";
        }

});


// function to prevent clicking on run button until both image and video are uploaded
window.onload = function() {
        // disabled run button

        // checking if files are uploaded to enable run button
         if(imageUploaded && videoUploaded) {
              // enable run button
         }
}
