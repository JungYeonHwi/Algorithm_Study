/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */

function getGCD(a, b) {
    while (b > 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

var gcdOfStrings = function (str1, str2) {
    let answer = '';

    if (str1 === str2) return str1;
    if (str1[0] !== str2[0]) return "";

    let len = getGCD(str1.length, str2.length);

    for (let i = 0; i < len; i++) {
        if (str1[i] === str2[i]) answer += str1[i];
        else break;
    }

    for (let i = 0; i < str1.length; i += answer.length) {
        let value = str1.substr(i, answer.length);
        if (value !== answer) return "";
    }
    for (let i = 0; i < str2.length; i += answer.length) {
        let value = str2.substr(i, answer.length);
        if (value !== answer) return "";
    }

    return answer;
};