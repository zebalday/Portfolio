

document.addEventListener("DOMContentLoaded", function() {
    var toggleBtn = document.getElementById("toggleBtn");
    var songList = document.getElementsByClassName("songItem");
    console.log(songList);

    toggleBtn.addEventListener("click", function() {
        
        
        Array.from(songList).forEach(song =>{
            
            if (song.classList.contains("hide")) {

                song.classList.remove("hide");
                song.classList.add("show");
                toggleBtn.innerText = "(hide)";
            }
            
            else {
                song.classList.remove("show");
                song.classList.add("hide");
                toggleBtn.innerText = "(show)";
            }
        });
    });
});


