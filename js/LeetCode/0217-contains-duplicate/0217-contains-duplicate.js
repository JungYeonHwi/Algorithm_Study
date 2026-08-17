/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let setNums = new Set([...nums]);
    return [...setNums].length === nums.length ? false : true;
};