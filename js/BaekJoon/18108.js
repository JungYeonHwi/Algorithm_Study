const fs = require("fs");
//let input = fs.readFileSync("input.txt").toString().trim();
let input = fs.readFileSync("/dev/stdin").toString().trim();

console.log(Number(input) - 543);
