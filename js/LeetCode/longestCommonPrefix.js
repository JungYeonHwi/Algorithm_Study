/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  if (strs.length == 0) {
    return "";
  }

  let preprefix = "";
  let answer = "";

  for (let i = 0; i < strs[0].length; i++) {
    answer += strs[0][i];
    for (let j = 0; j < strs.length; j++) {
      if (!strs[j].startsWith(answer)) {
        return preprefix;
      }
    }
    preprefix = answer;
  }

  return answer;
};
