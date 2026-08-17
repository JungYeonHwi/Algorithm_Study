/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let maxCount = 0;
    let answer = 0;

    let arr = [...new Set(nums)]
    for (let i = 0; i < arr.length; i ++) {
        let count = [...nums].filter(x => x === arr[i]).length;
        if (maxCount <= count) {
            maxCount = count;
            answer = arr[i];
        }
    }

    return answer;
};