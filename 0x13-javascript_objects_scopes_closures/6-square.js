#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let d = '';
      for (let j = 0; j < this.width; j++) {
        d += c;
      }
      console.log(d);
    }
  }
}

module.exports = Square;
