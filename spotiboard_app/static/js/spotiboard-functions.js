

document.addEventListener("DOMContentLoaded", function() {

    // TOOGLE BUTTON FOR LAST PLAYED SONGS
    var toggleBtnLastSongs = document.getElementById("toggleBtnLastSongs");
    var lastSongList = document.getElementsByClassName("last-song-item");
    
    toggleBtnLastSongs.addEventListener("click", function() {
        
        Array.from(lastSongList).forEach(song =>{
            
            if (song.classList.contains("hide")) {

                song.classList.remove("hide");
                song.classList.add("show");
                toggleBtnLastSongs.innerText = "(hide)";
            }
            
            else {
                song.classList.remove("show");
                song.classList.add("hide");
                toggleBtnLastSongs.innerText = "(show)";
            }
        });
    });
    

    // TOOGLE BUTTON FOR USER TOP ARTISTS
    var toggleBtnTopArtists = document.getElementById("toggleBtnTopArtists");
    var topArtistsList = document.getElementsByClassName("top-artist-card");
    console.log(topArtistsList)

    toggleBtnTopArtists.addEventListener("click", function(){

        Array.from(topArtistsList).forEach(artistCard =>{
            
            if (artistCard.classList.contains("hide")) {

                artistCard.classList.remove("hide");
                artistCard.classList.add("show");
                toggleBtnTopArtists.innerText = "(hide)";
            }
            
            else {
                artistCard.classList.remove("show");
                artistCard.classList.add("hide");
                toggleBtnTopArtists.innerText = "(show)";
            }
        });
    });
});


