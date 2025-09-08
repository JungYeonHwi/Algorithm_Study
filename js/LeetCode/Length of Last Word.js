/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  let arr = s.split(" ");
  arr = arr.filter((item) => item !== "");
  return arr[arr.length - 1].length;
};
