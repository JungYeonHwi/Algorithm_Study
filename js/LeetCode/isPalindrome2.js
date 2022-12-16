/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  s = s.replace(/[^a-zA-Z0-9]/g, "");
  s = s.toLowerCase();

  let arr = s.split("");
  let reversed = s.split("").reverse();

  if (arr.toString() == reversed.toString()) {
    return true;
  } else {
    return false;
  }
};
