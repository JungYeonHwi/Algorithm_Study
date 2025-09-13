/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let bin = n.toString(2);
  let regex = /1/g;
  let arr = bin.match(regex); // 0이면 null값이 들어옴
  let count = arr === null ? 0 : arr.length;

  return count;
};
