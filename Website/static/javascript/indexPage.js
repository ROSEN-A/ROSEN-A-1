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