/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  strs.sort((a, b) => a.length - b.length);
  if (strs.length === 1) return strs[0];
  if (strs.includes("")) return "";

  let arr = [];
  let answer = "";
  for (let k = 0; k < strs[0].length; k++) {
    let check = true;
    for (let j = 1; j < strs.length; j++) {
      if (strs[j][k] !== strs[0][k]) check = false;
    }

    if (check) answer += strs[0][k];
    else break;
  }

  return answer;
};
