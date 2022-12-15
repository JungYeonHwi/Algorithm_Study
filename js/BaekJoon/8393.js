const fs = require("fs");
//let input = fs.readFileSync("input.txt").toString();
let input = fs.readFileSync("/dev/stdin").toString();

let num = Number(input);
let answer = 0;

for (let i = 1; i < num + 1; i++) {
  answer += i;
}

console.log(answer);
