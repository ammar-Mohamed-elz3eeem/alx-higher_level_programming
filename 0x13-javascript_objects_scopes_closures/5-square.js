#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Sqaure extends Rectangle {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }
};
