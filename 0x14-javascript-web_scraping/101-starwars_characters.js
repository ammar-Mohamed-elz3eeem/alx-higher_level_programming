#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function get_request(url) {
  return new Promise((resolve, reject) => {
    request(url, (err, response) => {
      if (err) {
        reject(err);
      }
      resolve(JSON.parse(response.body));
    })
  })
}

// request(url, (err, res) => {
//   if (err) {
//     console.log(err);
//     process.exit();
//   }
//   const data = JSON.parse(res.body);
//   const characters = data.characters;

//   characters.forEach(async (charchter) => {
//     const charInfo = await get_request(charchter);
//     console.log(charInfo.name);
//   });
// });

async function get_chars(url) {
  const movieData = await get_request(url);
  const charchters = movieData.characters;
  const requests = [];
  charchters.forEach(async (charchter) => {
    const charchterInfo = get_request(charchter)
    requests.push(charchterInfo);
  })
  const all = Promise.all(requests);
  all.then(data => {
    data.forEach(charchterInfo => {
      console.log(charchterInfo.name)
    })
  })
}

get_chars(url);
