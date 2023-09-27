#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`API request failed with status code ${response.statusCode}`);
    return;
  }

  const filmsData = JSON.parse(body);
  const filmsWithWedgeAntilles = filmsData.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(filmsWithWedgeAntilles.length);
});
