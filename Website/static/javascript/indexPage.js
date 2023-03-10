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
        var video = document.querySelector("video");
        var button = document.querySelector("#run-button");
        var previewText = document.querySelector("#dragText");
        // console.log(video.src);
        if(!video.src) {
                button.setAttribute("disabled", "");
                previewText.style.display = "block";
        } else {
                button.removeAttribute("disabled");
                previewText.style.display = "none";
        }
}
