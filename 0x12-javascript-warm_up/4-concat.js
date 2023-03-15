#!/usr/bin/node
const process = require('process');

let var1 = 'undefined';
let var2 = 'undefined';
if (process.argv[2]) {
  var1 = process.argv[2];
}
if (process.argv[3]) {
  var2 = process.argv[3];
}
console.log(var1, 'is', var2);
