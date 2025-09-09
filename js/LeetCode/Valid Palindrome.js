/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const regex = /[^a-zA-Z0-9가-힣ㄱ-ㅎ]/g;

  const val = s.replaceAll(regex, "").toLowerCase();

  return val === [...val].reverse().join("") ? true : false;
};
