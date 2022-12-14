const fs = require("fs");
//let input = fs.readFileSync("input.txt").toString().trim();
let input = fs.readFileSync("/dev/stdin").toString().trim();

let cp = [1, 1, 2, 2, 2, 8];
arr = input.split(" ");

let answer = [];

for (let i = 0; i < 6; i++) {
  answer.push(cp[i] - arr[i]);
}

console.log(...answer);
