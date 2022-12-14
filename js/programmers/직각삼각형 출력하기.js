const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  let data = "";
  let n = Number(input[0]);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j <= i; j++) {
      data += "*";
    }
    data += "\n";
  }
  console.log(data);
});
