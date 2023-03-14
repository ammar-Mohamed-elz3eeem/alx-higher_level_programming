#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = Object.fromEntries(Object.entries(dict).map(el => [el[1], []]));
Object.keys(dict).map(key => newdict[dict[key]].push(key));
console.log(newdict);
