#!/usr/bin/node
/*
This script prints all character of Star Wars movie
*/
const request = require('request');

const ID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;

// endpoint = 'films/7'
request(url, function (error, _response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const charatersUrls = data.characters;

  if (!charatersUrls || !Array.isArray(charatersUrls)) {
    console.log('Error: charactor not found not in the  array');
  }
  const charactersMap = new Map();

  charatersUrls.forEach((url, index) => {
    request(url, function (error, _response, body) {
      if (error) {
        console.log(error);
        return;
      }
      const character = JSON.parse(body);
      charactersMap.set(url, {
        name: character.name,
        order: index
      });

      if (charactersMap.size === charatersUrls.length) {
        const sortedCharacters = Array.from(charactersMap.values()).sort((a, b) => a.order - b.order);
        sortedCharacters.forEach(character => console.log(character.name));
      }
    });
  });
});
