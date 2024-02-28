// fetches and lists the title for all moviess and then inserts
// into the UL#list_movies

$.get('https://swapi.co/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
