#!/usr/bin/node
const fs = require('fs');

const fAContent = fs.readFileSync(process.argv[2]).toString();
const fBContent = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fAContent + fBContent);
