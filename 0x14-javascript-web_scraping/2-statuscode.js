#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response) => {
  if (!error && response.statusCode) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.error('Error:', error || 'Unknown error');
  }
});
