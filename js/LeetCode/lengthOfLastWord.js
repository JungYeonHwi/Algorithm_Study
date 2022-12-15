/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  let arr = s.trim().split(" ");
  let answer = 0;

  for (let i = 0; i < arr.length; i++) {
    answer = arr[i].length;
  }

  return answer;
};
