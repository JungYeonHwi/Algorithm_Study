/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  let dict = {};
  let answer = 0;

  nums.forEach(function (i) {
    if (dict[i]) {
      dict[i] += 1;
    } else {
      dict[i] = 1;
    }
  });

  let m = parseInt(nums.length / 2);

  for (var key in dict) {
    if (m <= dict[key]) {
      answer = key;
      m = dict[key];
    }
  }

  return answer;
};
