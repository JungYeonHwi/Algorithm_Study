/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
  var result = [];
  for (var i = 0; i <= rowIndex; i++) {
    result[i] = [];
  }
  for (i = 0; i <= rowIndex; i++) {
    result[i][0] = result[i][i] = 1;
  }
  for (i = 2; i <= rowIndex; i++) {
    for (var j = 1; j < i; j++) {
      result[i][j] = result[i - 1][j - 1] + result[i - 1][j];
    }
  }
  return result[rowIndex];
};
