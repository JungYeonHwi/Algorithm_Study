/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    let ss = '';
    let tt = '';

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '#') ss = ss.slice(0, -1)
        else ss += s[i];
    }

    for (let i = 0; i < t.length; i++) {
        if (t[i] === '#') tt = tt.slice(0, -1)
        else tt += t[i];
    }

    return ss === tt;
};