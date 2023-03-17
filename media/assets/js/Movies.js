let Api;

async function getApi(){
let res= await fetch(`https://api.themoviedb.org/3/trending/movie/day?api_key=d903bcdae97d41411a8e54f49fb3b5d0`)
let finalRes = await res.json()
Api = finalRes.results
displayMovies()
}
getApi()



function displayMovies(){
    let container= ``
    for( let i=0 ; i<Api.length; i++){
        container+= `
        <div class="col-md-3">
        <div class="movie position-relative shadow-lg rounded">
            <div class="rate position-absolute end-0 top-0">
                <span>${Api[i].vote_average}</span>
            </div>
            <img class=" card-img-top w-100" src="https://image.tmdb.org/t/p/w500/${Api[i].poster_path}" alt="">
        </div>
    </div>`
    }
    document.getElementById('showData').innerHTML=container
    
}

// -----------------------
$(document).ready(()=> $('body').css('overflow' , 'auto'))





