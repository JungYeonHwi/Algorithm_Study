const fs = require("fs");
const [x, y] = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let pos;

if (x > 0 && y > 0) {
  pos = 1;
} else if (x < 0 && y > 0) {
  pos = 2;
} else if (x < 0 && y < 0) {
  pos = 3;
} else {
  pos = 4;
}

console.log(pos);
