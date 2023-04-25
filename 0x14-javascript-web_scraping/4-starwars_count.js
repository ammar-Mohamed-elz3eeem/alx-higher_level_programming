#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (err, res) => {
  if (err) {
    console.log(err);
    process.exit();
  }
  const data = JSON.parse(res.body);
  console.log(data.results.filter((val) => val.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length);
});
