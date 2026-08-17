/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        let a = nums[i];
        let remain = target - a;

        if (nums.includes(remain) && nums.indexOf(remain) !== i && nums.indexOf(remain) !== -1) {
            return [i, nums.indexOf(remain)];
        } 
    }
};