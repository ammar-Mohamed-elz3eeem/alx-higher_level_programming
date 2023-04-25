#!/usr/bin/node
const fs = require("fs");
const reader = fs.readFile(process.argv[2], {encoding:"utf-8"}, (err, data) => {
	if (err) {
		console.log(err)
		process.exit()
	}
	console.log(data)
})
