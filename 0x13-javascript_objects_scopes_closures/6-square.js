#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let height = '';
      for (let j = 0; j < this.width; j++) {
        if (undefined === c) {
          height += 'X';
        } else {
          height += c;
        }
      }
      console.log(height);
    }
  }
};
