    const menu = document.getElementById("menu");
    const toggle = document.getElementById("toggle");
    
    document.getElementById("toggle").addEventListener("click", function() {
        
        toggle.children[0].setAttribute("style","--fa-rotate-angle:0deg")

        if (menu.classList.contains("show-menu")) {
            menu.className = menu.className.replace("show-menu", "hide-menu");
            toggle.children[0].setAttribute("style","--fa-rotate-angle:0deg")
        }
        else if(menu.classList.contains("hide-menu")){
            menu.className = menu.className.replace("hide-menu", "show-menu");
            toggle.children[0].setAttribute("style","--fa-rotate-angle:45deg")
        }
    });
    