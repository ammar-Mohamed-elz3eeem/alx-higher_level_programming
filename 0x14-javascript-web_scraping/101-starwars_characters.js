#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, response) => {
      if (err) {
        reject(err);
      }
      resolve(JSON.parse(response.body));
    });
  });
}

async function getChars (url) {
  const movieData = await getRequest(url);
  const charchters = movieData.characters;
  const requests = [];
  charchters.forEach(async (charchter) => {
    const charchterInfo = getRequest(charchter);
    requests.push(charchterInfo);
  });
  const all = Promise.all(requests);
  all.then(data => {
    data.forEach(charchterInfo => {
      console.log(charchterInfo.name);
    });
  });
}

getChars(url);
