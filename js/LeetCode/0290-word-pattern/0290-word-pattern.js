/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function (pattern, s) {
    let map = new Map();
    let arr = s.split(" ");
    let str = '';

    for (let i = 0; i < arr.length; i++) {
        if (!map.has(arr[i])) {
            if (Array.from(map.values()).includes(pattern[i])) return false;
            map.set(arr[i], pattern[i])
            str += pattern[i];
        } else {
            if (map.get(arr[i]) !== pattern[i]) return false;
            str += map.get(arr[i]);
        }
    }

    return str === pattern;

};