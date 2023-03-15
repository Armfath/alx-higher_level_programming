#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let length = '';
    for (let i = 0; i < this.width; i++) {
      length += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(length);
    }
  }
}

module.exports = Rectangle;
