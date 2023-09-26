#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const starApi = argv[2];
const character = 'https://swapi-api.hbtn.io/api/people/18/';

request(starApi, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  let count = 0;

  const data = JSON.parse(body);

  if (data.results) {
    for (const film of data.results) {
      if (film.characters.includes(character)) {
        count++;
      }
    }
  }

  console.log(count);
});
