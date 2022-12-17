/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function (columnTitle) {
  let answer = 0;
  for (let i = columnTitle.length - 1, k = 0; i >= 0; i--, k++) {
    answer += (columnTitle.charCodeAt(i) - 64) * 26 ** k;
  }
  return answer;
};
