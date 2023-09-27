#!/usr/bin/node

const request = require('request');

const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const WEDGE_ANTILLES_ID = 18;

const urlWithFilter = `${API_URL}?characters=${WEDGE_ANTILLES_ID}`;

request.get(urlWithFilter, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const filmsData = JSON.parse(body);

  const numMovies = filmsData.count;

  console.log(numMovies);
});
