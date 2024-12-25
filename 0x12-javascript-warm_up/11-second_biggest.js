#!/usr/bin/node

const args = process.argv.slice(2);
const Numbers = args.map(Number).filter(num => !isNaN(num));

if (Numbers.length < 2) {
  console.log(0);
} else {
    Numbers.sort((a, b) => b - a);

    console.log(Numbers[1]);
}
