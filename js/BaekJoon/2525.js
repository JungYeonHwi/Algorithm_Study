const fs = require("fs");
//const input = fs.readFileSync("input.txt").toString().trim().split("\n");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const current = input[0].split(" ").map(Number);

let A = current[0];
let B = current[1];
let C = Number(input[1]);

A += parseInt(C / 60);
B += C % 60;

if (B >= 60) {
  A += 1;
  B -= 60;
}

if (A >= 24) {
  A -= 24;
}

console.log(String(A), String(B));
