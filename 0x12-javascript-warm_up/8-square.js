#!/usr/bin/node
const process = require('process');

if (!process.argv[2] || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  let length = '';
  for (let j = 0; j < size; j++) {
    length += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(length);
  }
}
