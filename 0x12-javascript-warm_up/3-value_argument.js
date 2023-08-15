#!/usr/bin/node

const myArg = process.argv.slice(2);

if (myArg[0] === undefined) {
  console.log('No argument');
} else {
  console.log(myArg[0]);
}
