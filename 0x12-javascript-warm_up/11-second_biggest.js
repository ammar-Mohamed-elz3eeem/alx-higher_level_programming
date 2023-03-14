#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const argv = [];
  for (let i = 2; i < process.argv.length; i++) {
    argv.push(parseInt(process.argv[i]));
  }

  console.log(argv.sort((a, b) => b - a)[1]);
}
