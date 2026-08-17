/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let answer = '';
    strs = strs.sort((a, b) => a.length - b.length);
    let len = strs[0].length;

    for (let i = 0; i < len; i++) {
        let char = strs[0][i];
        let isCommon = strs.every(str => str[i] === char);
        
        if (isCommon) {
            answer += char;
        } else {
            break;
        }
    }

    return answer;
};