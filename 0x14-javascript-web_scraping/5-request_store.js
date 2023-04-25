#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url, (err, _res, body) => {
  if (err) {
    console.log(err);
    process.exit();
  }
  fs.writeFile(process.argv[3], body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.log(err);
      process.exit();
    }
  });
});
