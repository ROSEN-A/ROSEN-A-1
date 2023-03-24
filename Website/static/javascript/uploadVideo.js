(function Preview_Video() {
        'use strict'
var URL = window.URL || window.webkitURL


var Play_Video = function (event) {
var file = this.files[0]
var type = file.type
var videoNode = document.querySelector('video')
var fileURL = URL.createObjectURL(file)
videoNode.src = fileURL
}

var inputNode = document.querySelector('input')
inputNode.addEventListener('change', Play_Video, false)
})()

window.onload = function() {
        var dragArea = document.querySelector(".drag-area-video");
        var video = document.querySelector(".drag-area-video video");
        var button = document.querySelector("#run-button");
        var previewText = document.querySelector("#dragText");
        console.log(video.src);
        if(!video.src) {
                button.setAttribute("disabled", "");
                previewText.style.display = "block";
                dragArea.classList.remove("active");
        } else {
                button.removeAttribute("disabled");
                previewText.style.display = "none";
                dragArea.classList.add("active");
        }
}




function invalidFileType() {
        var form = document.querySelector("form");
        var file = document.querySelector("#file");
                if(!file.files[0].type.match("video/*")) {
                        alert("Invalid file type!");
                }
}
