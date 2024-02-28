// fetches and lists the title for all moviess and then inserts
// into the UL#list_movies

let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
    let films = data.results;
    for (let film of films) {
        $('ul#list_movies').append(`<li>${film.title}</li>`);
    }
});
