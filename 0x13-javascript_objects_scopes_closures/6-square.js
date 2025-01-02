#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
