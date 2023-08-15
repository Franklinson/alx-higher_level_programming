#!/usr/bin/node

const myArg = process.argv[2];

const parsedInt = parseInt(myArg);

if (!isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
