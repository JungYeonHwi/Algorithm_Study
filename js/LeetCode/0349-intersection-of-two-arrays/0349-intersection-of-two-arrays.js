/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
    let n1 = [...new Set(nums1)];
    let n2 = [...new Set(nums2)];
    let answer = [];

    let len = Math.min(n1.length, n2.length);
    let who = len === n1.length ? n1 : n2;
    let remain = len !== n1.length ? n1 : n2;

    console.log(len, who, remain)

    for (let i = 0; i < len; i++) {
        if (remain.includes(who[i])) answer.push(who[i]);
    }

    return answer;
};