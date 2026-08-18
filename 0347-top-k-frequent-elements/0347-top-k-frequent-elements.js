/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    let set = [...new Set(nums)];
    let map = new Map();

    for (let i = 0; i < set.length; i++) {
        let count = [...nums].filter(x => x === set[i]);
        map.set(set[i], count);
    }

    const sortedArray = [...map.values()].sort((a, b) => b.length - a.length);
    const sortedMap = new Map(sortedArray);
    const slicedMap = new Map(
        Array.from(sortedMap.entries()).slice(0, k)
    );

    return Array.from(slicedMap.keys());

};