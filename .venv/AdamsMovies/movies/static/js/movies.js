document.addEventListener("DOMContentLoaded", loaded);

const movies = ["something", "nothing", "some movie", "some other movie"];
const moviesW = ["movie1", "movie2", "movie3", "movie4"];

function loaded() {
    moviesToWatch()
}

function moviesToWatch() {
    
    let size = movies.length;
    let text = "";
    for(var i = 0; i < size; i++) {
        text += "-  " + movies[i] + "<br>";
    }
    document.getElementById("MoviesTW").innerHTML = text;
}

function moviesWatched() {
    

      let sizeW = moviesW.length;
      let textW = "";
      for(var i = 0; i < sizeW; i++) {
          textW += "-  " + moviesW[i] + "<br>";
      }
      document.getElementById("MoviesW").innerHTML = textW;
}

function random() {
    let randIndex = Math.floor(Math.random() * sizeW); 
    document.getElementById("randMovie").innerHTML = movies[randIndex];
}