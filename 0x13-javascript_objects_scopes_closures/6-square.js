#!/usr/bin/node
const SQ = require('./5-square');
module.exports = class Square extends SQ {
  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let height = '';
      for (let j = 0; j < this.size; j++) {
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
