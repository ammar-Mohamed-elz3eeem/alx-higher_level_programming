#!/usr/bin/node
module.exports = {
  converter (toBase) {
    return function (number) {
      return number.toString(toBase);
    };
  }
};
