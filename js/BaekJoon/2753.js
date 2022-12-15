const fs = require("fs");

//let input = fs.readFileSync("input.txt").toString().trim();
let input = fs.readFileSync("/dev/stdin").toString().trim();

year = Number(input);

if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
  console.log(1);
} else {
  console.log(0);
}
