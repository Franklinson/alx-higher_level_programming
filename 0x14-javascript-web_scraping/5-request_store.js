#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const argv = process.argv;
if (argv.length !== 4) {
  console.error('Usage: node fetchAndSaveWebpage.js <URL> <outputFilePath>');
  process.exit(1);
}

const url = argv[2];
const file = argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('HTTP Status Code:', response.statusCode);
    process.exit(1);
  }

  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      process.exit(1); // Exit the script on error
    }
    console.log(`Webpage content saved to ${file}`);
  });
});
