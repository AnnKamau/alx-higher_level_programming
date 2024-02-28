// fetches the character name of API data then replaces the name
// of the character in DIV#character tag

let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data, stat) {
    $('div#character').text(data.name);
});
