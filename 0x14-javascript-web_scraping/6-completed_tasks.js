#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res) => {
  if (err) {
    console.log(err);
    process.exit();
  }
  const data = JSON.parse(res.body);
  const returned = {};
  data.forEach(element => {
    if (element.completed === true) {
      if (returned[element.userId]) {
        returned[element.userId]++;
      } else {
        returned[element.userId] = 1;
      }
    }
  });
  console.log(returned);
});
