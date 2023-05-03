#!/usr/bin/node
/*
This script prints all character of Star Wars movie
position arguent : Movie ID
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
    console.log('Error: character not found not in the  array');
  }
  const charactersMap = new Map();

  { /*
    getting character for each chracter filtered from character url
    checking for character in each Url
    */ }
  charatersUrls.forEach((url, index) => {
    request(url, function (error, _response, body) {
      if (error) {
        console.log(error);
        return;
      }

      { /*
      variable pass characters in json format
      mapping characters in set of name and order
      :according to character index
    */ }

      const character = JSON.parse(body);
      charactersMap.set(url, {
        name: character.name,
        order: index
      });

      { /*
        check if all charactersUrls have been processed by request
        and pass the to sortedCharacters array then sorted in order property
        in ascending order , and print each in an ascending order
    */ }

      if (charactersMap.size === charatersUrls.length) {
        const sortedCharacters = Array.from(charactersMap.values()).sort((a, b) => a.order - b.order);
        sortedCharacters.forEach(character => console.log(character.name));
      }
    });
  });
});
