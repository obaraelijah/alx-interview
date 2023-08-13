#!/usr/bin/node

import request from 'request';

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode === 200) {
    (async function () {
      const characters = JSON.parse(body).characters;

      try {
        const responses = await Promise.all(
          characters.map((character) => requestCharacter(character))
        );

        for (const response of responses) {
          console.log(response.name);
        }
      } catch (error) {
        console.error(error);
      }
    })();
  }
});

function requestCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode === 200) {
        resolve(JSON.parse(body));
      }
    });
  });
}