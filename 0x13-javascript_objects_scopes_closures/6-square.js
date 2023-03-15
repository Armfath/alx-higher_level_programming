#!/usr/bin/node
const Squar = require('./5-square');

class Square extends Squar {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let length = '';
    for (let i = 0; i < this.width; i++) {
      length += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(length);
    }
  }
}

module.exports = Square;
