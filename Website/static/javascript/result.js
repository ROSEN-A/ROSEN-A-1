
$(document).ready(function() {
    $(".image").on("mouseover", function() {
        var src = $(this).attr("src");
        var preview = $("<div id='preview'></div>");
        var image = $("<img src='" + src +"'>");
        preview.append(image);
        preview.css({"display" : "block", "position": "fixed", "width" : "200px", "left": "0", "bottom": "0", "z-index" : "99"});
        image.css("width", "100%");
        $("body").append(preview);
    });
    $(".image").on("mouseleave", function() {
        $("#preview").fadeOut("normal", function() {
            $("#preview").remove();
        });
    });
});
