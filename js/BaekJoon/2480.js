const fs = require("fs");

//const input = fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const [a, b, c] = [input[0], input[1], input[2]];

let answer;

if (a == b && b == c) {
  answer = 10000 + a * 1000;
} else if (a == b && b != c) {
  answer = 1000 + a * 100;
} else if (a == c && c != b) {
  answer = 1000 + c * 100;
} else if (b == c && a != b) {
  answer = 1000 + b * 100;
} else {
  answer = Math.max(a, b, c) * 100;
}

console.log(answer);
