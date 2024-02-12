#!/usr/bin/node

import request from 'request';

function getCharacters (movieId) {
  return new Promise((resolve, reject) => {
    request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch movie data for movie ID ${movieId}`));
      } else {
        const movieData = JSON.parse(body);
        const charactersUrls = movieData.characters;
        const characters = [];
        const fetchCharacterData = (charUrl) => {
          return new Promise((resolve, reject) => {
            request(charUrl, (error, response, body) => {
              if (error) {
                reject(error);
              } else if (response.statusCode !== 200) {
                reject(new Error(`Failed to fetch character data for ${charUrl}`));
              } else {
                const characterData = JSON.parse(body);
                characters.push(characterData.name);
                resolve();
              }
            });
          });
        };

        const promises = charactersUrls.map(fetchCharacterData);
        Promise.all(promises)
          .then(() => resolve(characters))
          .catch(error => reject(error));
      }
    });
  });
}

async function main () {
  const args = process.argv.slice(2);
  if (args.length !== 1 || isNaN(args[0])) {
    console.log('Usage: node script.js <movie_id>');
    process.exit(1);
  }

  const movieId = args[0];
  try {
    const characters = await getCharacters(movieId);
    characters.forEach(character => console.log(character));
  } catch (error) {
    console.error(error);
  }
}

main();
