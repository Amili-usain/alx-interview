#!/usr/bin/node

/**
 * This script retrieves and prints the names of characters from a Star Wars movie
 * in the same order as the "characters" list in the `/films/` endpoint.
 * The movie ID is passed as a command-line argument.
 */

const request = require('request');

/**
 * Fetches the characters from the Star Wars API and prints their names.
 * @param {string} movieId - The ID of the Star Wars movie.
 */
function printStarWarsCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, async function (error, response, body) {
    if (error) {
      return console.log(error);
    } else {
      const characters = JSON.parse(body).characters;
      for (const character in characters) {
        const res = await new Promise((resolve, reject) => {
          request(characters[character], (err, res, html) => {
            if (err) {
              reject(err);
            } else {
              resolve(JSON.parse(html).name);
            }
          });
        });
        console.log(res);
      }
    }
  });
}

// Retrieve the movie ID from the command-line argument
const movieId = process.argv[2];

// Call the function to fetch and print the Star Wars characters
printStarWarsCharacters(movieId);
