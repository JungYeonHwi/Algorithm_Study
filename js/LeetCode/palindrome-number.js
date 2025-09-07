/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) return false;
  else {
    if (String(x) === [...String(x)].reverse().join("")) return true;
    else return false;
  }
};
