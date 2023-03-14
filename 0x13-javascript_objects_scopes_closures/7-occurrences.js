#!/usr/bin/node
module.exports = {
  nbOccurences (list, searchElement) {
    let occured = 0;
    for (const el of list) {
      if (el === searchElement) occured++;
    }
    return occured;
  }
};
