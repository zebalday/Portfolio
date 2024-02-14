const menu = document.getElementById("menu");
const icon = document.getElementById("fa-caret-right");

document.getElementById("toggle").addEventListener("click", function() {
    
    if (menu.classList.contains("show-menu") || menu.classList.contains("")) {
        menu.className = menu.className.replace("show-menu", "hide-menu");
        icon.setAttribute("transform", "rotate(0)");
    }
    else if(menu.classList.contains("hide-menu")){
        menu.className = menu.className.replace("hide-menu", "show-menu");
        icon.setAttribute("transform", "rotate(90)");
    }
});
