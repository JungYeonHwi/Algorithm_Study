const fs = require("fs");
//let input = fs.readFileSync("input.txt").toString();
let input = fs.readFileSync("/dev/stdin").toString();

let num = Number(input[0]);

for (let i = 1; i < 10; i++) {
  console.log(`${num} * ${i} = ${num * i}`);
}
