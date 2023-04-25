#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (err, res) => {
  if (err) {
    console.log(err);
    process.exit();
  }
  const data = JSON.parse(res.body);
  let times = 0;
  data.results.forEach((val) => {
    for (let i = 0; i < val.characters.length; i++) {
      const charId = val.characters[i].split('/')[5];
      if (charId === '18') {
        times++;
      }
    }
  });
  console.log(times);
});
