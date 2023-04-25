#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (err, res) => {
  if (err) {
    console.log(err);
    process.exit();
  }
  const data = JSON.parse(res.body);
  const characters = data.characters;

  characters.forEach(charchter => {
    request(charchter, (err, res) => {
      if (err) {
        console.log(err);
        process.exit();
      }
      const charInfo = JSON.parse(res.body);
      console.log(charInfo.name);
    });
  });
});
