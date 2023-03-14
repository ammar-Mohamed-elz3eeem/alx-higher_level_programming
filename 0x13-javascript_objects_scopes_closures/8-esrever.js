#!/usr/bin/node
module.exports = {
  esrever (list) {
    let newlist = [];
    for (const el of list) {
      newlist = [el, ...newlist];
    }
    return newlist;
  }
};
