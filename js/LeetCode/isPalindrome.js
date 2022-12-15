/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  let origin = String(x).split("");
  let reversed = String(x).split("").reverse();

  if (origin.join("") == reversed.join("")) {
    return true;
  } else {
    return false;
  }
};
