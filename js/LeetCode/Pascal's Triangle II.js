/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
  if (rowIndex === 0) return [1];
  if (rowIndex === 1) return [1, 1];

  let answer = [[0], [1], [1, 1]];
  for (let i = 3; i < rowIndex + 2; i++) {
    let temp = [1];
    for (let k = 1; k < i - 1; k++) {
      let val = answer[i - 1][k - 1] + answer[i - 1][k];
      temp.push(val);
    }
    temp.push(1);
    answer.push(temp);
  }

  answer = answer.slice(1);

  return answer[rowIndex];
};
