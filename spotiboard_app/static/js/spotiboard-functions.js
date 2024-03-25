

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
    var topArtistsContainer = document.getElementById("artists-cards");
    var topArtistsList = document.getElementsByClassName("top-artist-card");
    
    toggleBtnTopArtists.addEventListener("click", function(){
        
        if(topArtistsContainer.classList.contains("showFadeIn")){
            topArtistsContainer.classList.remove("showFadeIn");
            topArtistsContainer.classList.add("hideFadeOut");
        }
        
        else {
            topArtistsContainer.classList.add("showFadeIn");
            topArtistsContainer.classList.remove("hideFadeOut");
        }

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
    
    // TOOGLE BUTTON FOR TOP SONGS
    var toggleBtnTopSongs = document.getElementById("toggleBtnTopSongs");
    var topSongsList = document.getElementsByClassName("top-track-item");

    toggleBtnTopSongs.addEventListener("click", function(){

        Array.from(topSongsList).forEach(SongItem => {

            if(SongItem.classList.contains("showFadeIn")){
                SongItem.classList.remove("showFadeIn");
                SongItem.classList.add("hideFadeOut");            
                toggleBtnTopSongs.innerText = "(show)";
            }
            else{
                SongItem.classList.remove("hideFadeOut");
                SongItem.classList.add("showFadeIn");
                toggleBtnTopSongs.innerText = "(hide)";
            }
        });
    });
    
    // TOGGLE BUTTON FOR TOP GENRES
    var toggleBtnTopGenres = document.getElementById("toggleBtnTopGenres");
    var topGenresList = document.getElementsByClassName("top-genre-item");

    toggleBtnTopGenres.addEventListener("click", function(){

        Array.from(topGenresList).forEach(GenreItem =>{

            if(GenreItem.classList.contains("show")){
                GenreItem.classList.remove("show");
                GenreItem.classList.add("hide");
                toggleBtnTopGenres.innerText = "(show)";
            }
            else{
                GenreItem.classList.remove("hide");
                GenreItem.classList.add("show");
                toggleBtnTopGenres.innerText = "(hide)";
            }
        });
    });


    // TOGGLE FOR LAST ADDED SONGS
    var toggleBtnLastSavedSongs = document.getElementById("toggleBtnLastSavedSongs");
    var lastSavedSongList = document.getElementsByClassName("last-saved-song-item");

    toggleBtnLastSavedSongs.addEventListener("click", function(){

        Array.from(lastSavedSongList).forEach(SongItem => {

            if(SongItem.classList.contains("show")){
                SongItem.classList.remove("show");
                SongItem.classList.add("hide");
                toggleBtnLastSavedSongs.innerText = "(show)";
            }
            else{
                SongItem.classList.remove("hide");
                SongItem.classList.add("show");
                toggleBtnLastSavedSongs.innerText = "(hide)";
            }
        });
    });
});


