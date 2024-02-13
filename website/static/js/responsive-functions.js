const menu = document.getElementById("menu");

document.getElementById("toggle").addEventListener("click", function() {
    
    if (menu.classList.contains("show-menu") || menu.classList.contains("")) {
        menu.className = menu.className.replace("show-menu", "hide-menu");
    }
    else if(menu.classList.contains("hide-menu")){
        menu.className = menu.className.replace("hide-menu", "show-menu");
        menu.slideToggle();
    }
});
