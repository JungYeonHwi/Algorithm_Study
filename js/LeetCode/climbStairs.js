/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  if (n <= 2) {
    return n;
  }

  prevValue = 1;
  currValue = 2;

  for (let i = 2; i < n; i++) {
    tmp = currValue;
    currValue = prevValue + currValue;
    prevValue = tmp;
  }

  return currValue;
};
