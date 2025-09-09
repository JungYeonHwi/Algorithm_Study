/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function (columnNumber) {
  let total = columnNumber;
  let result = "";
  while (total > 0) {
    total--;
    const remain = total % 26;
    result = String.fromCharCode(65 + remain) + result;
    total = Math.floor(total / 26);
  }

  return result;
};
