document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll('.project-filters .filter');
    
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            var filterId = button.dataset.filter;
            /* alert(filterId); */
            // Remove 'active' class from all buttons
            buttons.forEach(function(btn) {
                btn.classList.remove('active');
            });
            
            // Add 'active' class to the clicked button
            button.classList.add('active');

            // PERFORM FILTERING USING JUST STYLES
            var projectCards = document.querySelectorAll(".projects-container .project-card");
            
            projectCards.forEach(function (projectCard){
                if(filterId === "*"){
                    if(projectCard.classList.contains("hide-card")){
                        projectCard.classList.replace("hide-card", "show-card");
                    }
                }
                else if (!projectCard.classList.contains(filterId)){
                    if(projectCard.classList.contains("hide-card")){
                        projectCard.classList.replace("hide-card", "show-card");
                    }
                    else{
                        projectCard.classList.add("hide-card");
                    }
                }
                else if(projectCard.classList.contains(filterId) && projectCard.classList.contains("hide-card")){
                    projectCard.classList.replace("hide-card", "show-card");
                }
                else if(projectCard.classList.contains("show-card")){
                    // Nothing
                }
            });
        });
    });
});