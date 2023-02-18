// currently all functions are not working, unable to test
window.onload = function() { 

    // function for image selection

    var images = document.getElementsByClassName("images")[0].children;

    // console.log(images[0]);

    for (let i = 0 ; i < 10 ; i++ ){
        images[i].addEventListener('click', function() {
            // let imagebox1 = document.getElementsByClassName("image-box image-box[" + i + "]")[0];
            if ( images[i].style.outline == "") {
                images[i].style.outline = "5px lightgreen solid";
            } else {
                images[i].style.outline = "";
            }
        });
    }



    // function for homepage redirect confirmation

    var homeButton = document.getElementById("homepage-button");
    var homeWarning = function(e) {
        if(!confirm("You will lose all your training progress. Proceed?")){
            e.preventDefault();
        }
    };
    homeButton.addEventListener("click", homeWarning, false);


    // rosen logo redirect confirmation

    var logo = document.getElementById("logo");
    var logoWarning = function(e) {
        if(!confirm("You will lose all your training progress. Proceed?")){
            e.preventDefault();
        }
    };
    logo.addEventListener("click", logoWarning, false);

    
    // logout redirect confirmation

    var logout = document.getElementById("logout-button");
    var logoutWarning = function(e) {
        if(!confirm("You will lose all your training progress. Proceed?")){
            e.preventDefault();
        }
    };
    logout.addEventListener("click", logoutWarning, false);


}



