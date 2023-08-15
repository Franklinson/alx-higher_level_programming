#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (myArgs.length === 0) {
  console.log('Missing number of occurrences');
} else {
  try {
    const occurrences = Number(myArgs[0]);

    for (let i = 0; i < occurrences; i++) {
      console.log('C is fun');
    }
  } catch (error) {
    console.log('Missing number of occurrences');
  }
}
