#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  constructor (size) {
    super(size, size);
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
