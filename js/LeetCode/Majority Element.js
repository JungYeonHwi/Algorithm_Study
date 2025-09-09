/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  let maxCount = nums.length / 2,
    count = 0;
  for (let i = 0; i < nums.length; i++) {
    count = 0;
    for (let j = 0; j < nums.length; j++) {
      if (nums[i] === nums[j]) count++;
    }
    if (count > maxCount) return nums[i];
  }
};
