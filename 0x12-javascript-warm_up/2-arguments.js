#!/usr/bin/node

const myArg = process.argv.length - 2;

if (myArg === 0) {
  console.log('No argument');
} else if (myArg === 1) {
 console.log('Argument found');
} else {
 console.log('Arguments found');
}
