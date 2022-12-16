/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  while (n) {
    nums1[m++] = nums2[--n];
  }
  nums1.sort(function (val1, val2) {
    return val1 > val2 ? 1 : val1 < val2 ? -1 : 0;
  });
};
