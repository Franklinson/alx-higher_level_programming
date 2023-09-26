#!/usr/bin/node

const fs = require('fs').promises;

async function writeStringToFile (filePath, content) {
  try {
    await fs.writeFile(filePath, content, 'utf-8');
    console.log(`String successfully written to ${filePath}`);
  } catch (err) {
    console.error(err);
  }
}

const [, , filePath, content] = process.argv;

if (!filePath || !content) {
  console.error('Usage: node script.js <file_path> <string_to_write>');
} else {
  writeStringToFile(filePath, content);
}
