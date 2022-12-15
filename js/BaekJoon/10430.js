const fs = require("fs");

//let [A, B, C] = fs.readFileSync("input.txt").toString().split(" ");
let [A, B, C] = fs.readFileSync("/dev/stdin").toString().split(" ");

A = Number(A);
B = Number(B);
C = Number(C);
console.log((A + B) % C);
console.log(((A % C) + (B % C)) % C);
console.log((A * B) % C);
console.log(((A % C) * (B % C)) % C);
