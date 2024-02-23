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
            
            switch(filterId){
                case "*":
                    projectCards.forEach(function (projectCard){
                        if (projectCard.classList.contains("hide-card")){
                            projectCard.classList.replace("hide-card","show-card");
                        }
                    });
                    break;
                case "filter-python":
                    projectCards.forEach(function (projectCard){
                        if (projectCard.classList.contains("filter-python")){
                            if(projectCard.classList.contains("hide-card")){
                                projectCard.classList.replace("hide-card","show-card");
                            }
                        }
                        else{
                            if(projectCard.classList.contains("show-card")){
                                projectCard.classList.replace("show-card","hide-card");
                            }
                            else if(!projectCard.classList.contains("show-card") || !projectCard.classList.contains("hide-card")){
                                projectCard.classList.add("hide-card");
                            }
                        }
                    });
                    break;
                case "filter-django":
                    projectCards.forEach(function (projectCard){
                        if (projectCard.classList.contains("filter-django")){
                            if(projectCard.classList.contains("hide-card")){
                                projectCard.classList.replace("hide-card","show-card");
                            }
                        }
                        else{
                            if(projectCard.classList.contains("show-card")){
                                projectCard.classList.replace("show-card","hide-card");
                            }
                            else if(!projectCard.classList.contains("show-card") || !projectCard.classList.contains("hide-card")){
                                projectCard.classList.add("hide-card");
                            }
                        }
                    });
                    break;
                case "filter-datascience":
                    projectCards.forEach(function (projectCard){
                        if (projectCard.classList.contains("filter-datascience")){
                            if(projectCard.classList.contains("hide-card")){
                                projectCard.classList.replace("hide-card","show-card");
                            }
                        }
                        else{
                            if(projectCard.classList.contains("show-card")){
                                projectCard.classList.replace("show-card","hide-card");
                            }
                            else if(!projectCard.classList.contains("show-card") || !projectCard.classList.contains("hide-card")){
                                projectCard.classList.add("hide-card");
                            }
                        }
                    });
                    break;
                default:
                    console.log("Error filtering.")
            }
        });
    });
});