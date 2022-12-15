const fs = require("fs");
//let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let x = Number(input[0]);
let n = Number(input[1]);
let sum = 0;

for (let i = 2; i <= n + 1; i++) {
  let arr = input[i].split(" ").map((value) => Number(value));
  sum += arr[0] * arr[1];
}

if (sum == x) {
  console.log("Yes");
} else {
  console.log("No");
}
