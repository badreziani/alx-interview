#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
