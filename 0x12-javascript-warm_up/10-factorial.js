#!/usr/bin/node

function myFact (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0 || n === 1) {
    return 1;
  }

  return n * myFact(n - 1);
}

const input = parseInt(process.argv[2]);
const factorial = myFact(input);

console.log(factorial);
