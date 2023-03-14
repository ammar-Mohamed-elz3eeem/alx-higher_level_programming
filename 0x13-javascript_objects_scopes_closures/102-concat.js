#!/usr/bin/node

if (process.argv.length >= 5) {
	const fs = require("fs");
	const fd1 = fs.openSync(process.argv[2]);
	const contents1 = fs.readFileSync(fd1).toString();
	const fd2 = fs.openSync(process.argv[3]);
	const contents2 = fs.readFileSync(fd2).toString();
	const fd3 = fs.openSync(process.argv[4], 'w');
	fs.writeFileSync(fd3, contents1 + '\n' + contents2);
} else {
	console.log(`Usage: ./102-concat.js file1 file2 file3`);
}
