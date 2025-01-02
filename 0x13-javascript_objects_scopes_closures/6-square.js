#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
  constructor (size) {
    super();
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
	let row = '';
	for (let j = 0; j < this.width; j++) {
	  console.log(c);
	}
      }
    }
    else print();
  }
}

module.exports = Square;
