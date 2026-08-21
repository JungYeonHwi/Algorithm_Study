/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let len = word1.length > word2.length ? word2.length : word1.length;
    let answer = '';

    for (let i = 0; i < len; i++) {
        answer += word1[i] + word2[i];
    }

    answer += word1.slice(len) + word2.slice(len);

    return answer;
};