/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  let dict = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let arr = s.split("");
  let answer = 0;

  for (let i = 0; i < arr.length; i++) {
    if (i > 0 && dict[arr[i]] > dict[arr[i - 1]]) {
      answer += dict[arr[i]] - 2 * dict[arr[i - 1]];
    } else {
      answer += dict[arr[i]];
    }
  }

  return answer;
};
