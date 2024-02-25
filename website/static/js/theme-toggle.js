// AGAIN
let currentTheme = "";
let currentHour = 0;
const lightTheme = document.querySelectorAll('link[rel="stylesheet"][href$="light.css"]');
const darkTheme = document.querySelectorAll('link[rel="stylesheet"][href$="dark.css"]');
const toggle = document.getElementById("theme-toggle");


// Set initial theme
function setInitialTheme(){
    // Set theme based on day hour
    const date = new Date();
    currentHour = date.getHours();
    if (currentHour >= 21 || currentHour <= 6) {
        currentTheme = "dark";
    } else {
        currentTheme = "light";
    }

    // Disable unused theme
    if(currentTheme === "light"){
        darkTheme[0].setAttribute("disabled",true);
    }
    else{
        lightTheme[0].setAttribute("disabled",true);
    }
}

// Event change theme
function toggleTheme(){

    if(currentTheme === "light"){
        // Change theme to light
        lightTheme[0].setAttribute("disabled",true);
        darkTheme[0].removeAttribute("disabled");
        currentTheme = "dark";
    }
    else if (currentTheme === "dark"){
        // Change theme to nigth
        darkTheme[0].setAttribute("disabled",true);
        lightTheme[0].removeAttribute("disabled");
        currentTheme = "light";
    }
}


window.addEventListener('DOMContentLoaded', () => {
    setInitialTheme();

    toggle.addEventListener("click", function(){
        toggleTheme();
    });


    
});


