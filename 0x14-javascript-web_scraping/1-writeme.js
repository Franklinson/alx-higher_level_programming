#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];
const content = process.argv[3];

if (!filename || !content) {
  console.error('Usage: node script.js <file-path> <content>');
} else {
  fs.writeFile(filename, content, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
}
