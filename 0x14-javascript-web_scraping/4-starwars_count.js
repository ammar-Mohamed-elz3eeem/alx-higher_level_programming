#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
let times = 0;
request(url, (err, res) => {
  if (err) {
    console.log(err);
    process.exit();
  }
  const data = JSON.parse(res.body).results;

  for (let i = 0; i < data.length; i++) {
    const chars = data[i].characters;

    for (let j = 0; j < chars.length; j++) {
      const char = chars[j];
      const charId = char.split('/')[5];

      if (charId === '18') {
        times++;
      }
    }
  }
  console.log(times);
});
