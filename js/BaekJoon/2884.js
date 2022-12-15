const fs = require("fs");

//let [A, B] = fs.readFileSync("input.txt").toString().split(" ");
let [A, B] = fs.readFileSync("/dev/stdin").toString().split(" ");

A = Number(A);
B = Number(B);

if (B >= 45) {
  B = B - 45;
} else {
  if (A == 0) {
    A = 23;
    B = B + 15;
  } else {
    A = A - 1;
    B = B + 15;
  }
}

console.log(String(A) + " " + String(B));
