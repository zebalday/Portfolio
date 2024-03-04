// Vars
let currentTheme = "";
let currentHour = 0;
const lightTheme = document.querySelectorAll('link[rel="stylesheet"][href$="light.css"]');
const darkTheme = document.querySelectorAll('link[rel="stylesheet"][href$="dark.css"]');
const toggle = document.getElementById("theme-toggle");

// Theme cookie
function createCookie(name,value,days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else var expires = "";
    document.cookie = name+"="+value+expires+"; path=/cookies";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function updateCookie(name, value){
    document.cookie = name + "=" + value + ";";
}

// Set initial theme
function setInitialTheme(){

    // Set theme based on cookie value
    if (readCookie("theme") != null){
        currentTheme = readCookie("theme")
    }
    // Set theme based on day hour
    else{
        const date = new Date();
        currentHour = date.getHours();
        if (currentHour >= 20 || currentHour <= 6) {
            currentTheme = "dark";
            createCookie("theme","dark",30);
        } else {
            currentTheme = "light";
            createCookie("theme","light",30);
        }
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
        updateCookie("theme","dark");
    }
    else if (currentTheme === "dark"){
        // Change theme to nigth
        darkTheme[0].setAttribute("disabled",true);
        lightTheme[0].removeAttribute("disabled");
        currentTheme = "light";
        updateCookie("theme","light");
    }
}


window.addEventListener('DOMContentLoaded', () => {
    setInitialTheme();

    toggle.addEventListener("click", function(){
        toggleTheme();
    });
});


