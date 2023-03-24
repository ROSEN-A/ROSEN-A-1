
window.onload = function() {
        var dragArea = document.querySelector(".drag-area-photo");
        var img = document.querySelector(".drag-area-photo img");
        var button = document.querySelector("#run-button");
        var previewText = document.querySelector("#dragText");

        if(!img.src) {
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
                if(!file.files[0].type.match("image/*")) {
                        alert("Invalid file type!");
                }
}
