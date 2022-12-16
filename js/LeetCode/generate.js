/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  let outer = [];
  let line = [1];
  for (let i = 0; i < numRows; i++) {
    let temp = [];
    outer.push(line);
    for (let j = 0; j < line.length; j++) {
      if (line[j + 1] !== undefined) {
        temp.push(line[j] + line[j + 1]);
      } else {
        temp.push(line[j] + 0);
      }
    }
    line = [1, ...temp];
  }
  return outer;
};
