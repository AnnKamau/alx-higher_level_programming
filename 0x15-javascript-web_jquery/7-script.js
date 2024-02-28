// fetches the character name of API data then replaces the name
// of the character in DIV#character tag

$.get('https://swapi.co/api/people/5/?format=json', function (data) {
    $('div#character').text(data.name);
});
