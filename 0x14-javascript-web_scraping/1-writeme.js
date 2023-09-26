#!/usr/bin/node

const fs = require('fs').promises;

const [filePath, content] = process.argv.slice(2);

if (!filePath || !content) {
  console.error('Usage: node script.js <file-path> <content>');
} else {
  (async () => {
    try {
      await fs.writeFile(filePath, content, 'utf-8');
    } catch (error) {
      console.error(error);
    }
  })();
}
