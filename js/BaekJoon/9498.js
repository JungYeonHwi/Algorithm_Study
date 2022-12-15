const fs = require("fs");

//let input = fs.readFileSync("input.txt").toString().trim();
let input = fs.readFileSync("/dev/stdin").toString().trim();

grade = Number(input);

if (100 >= grade && grade >= 90) {
  console.log("A");
} else if (90 > grade && grade >= 80) {
  console.log("B");
} else if (80 > grade && grade >= 70) {
  console.log("C");
} else if (70 > grade && grade >= 60) {
  console.log("D");
} else {
  console.log("F");
}
