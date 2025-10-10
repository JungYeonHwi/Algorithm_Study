const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  let value1 = `a = ${input[0]}`;
  let value2 = `b = ${input[1]}`;
  console.log(value1);
  console.log(value2);
});
