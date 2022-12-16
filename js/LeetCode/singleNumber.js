/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  let check = {};

  nums.forEach(function (i) {
    if (check[i]) {
      check[i] += 1;
    } else {
      check[i] = 1;
    }
  });

  for (var key in check) {
    if (check[key] == 1) {
      return key;
    }
  }
};
