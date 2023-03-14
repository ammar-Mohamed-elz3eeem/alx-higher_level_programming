#!/usr/bin/node

function logger() {
	let idx = 0;
	return () => {
		return idx++;
	}
}

const loggerVar = logger();

module.exports = {
	logMe (str) {
		let x = 0;
		console.log(`${loggerVar()}: ${str}`);
	}
}
