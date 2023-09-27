#!/usr/bin/node
const fs = require('fs');
const request = require('request');

if (process.argv.length !== 4) {
  console.error('Usage: node fetchAndSaveWebpage.js <URL> <outputFilePath>');
  process.exit(1);
}

request(process.argv[2])
  .on('error', (error) => {
    console.error('Error:', error);
    process.exit(1);
  })
  .pipe(fs.createWriteStream(process.argv[3]))
  .on('error', (error) => {
    console.error('Error writing to file:', error);
    process.exit(1);
  })
  .on('finish', () => {
    console.log(`Webpage content saved to ${process.argv[3]}`);
  });
