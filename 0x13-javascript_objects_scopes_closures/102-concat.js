#!/usr/bin/node
const fs = require('fs');

const [, , sourceFile1, sourceFile2, destination] = process.argv;
const data1 = fs.readFileSync(sourceFile1);
const data2 = fs.readFileSync(sourceFile2);
const concatenatedData = Buffer.concat([data1, data2]);
fs.writeFileSync(destination, concatenatedData);
