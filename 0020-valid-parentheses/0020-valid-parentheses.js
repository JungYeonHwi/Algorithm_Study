/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    let front = ['(', '{', '['];
    let back = [')', '}', ']'];

    let answer = true;

    for (let i = 0; i < s.length; i++) {
        console.log(s[i])
        let value = s[i];

        if (front.includes(value)) {
            stack.push(value);
        } else {
            let removed = stack.pop();
            let removedIndex = front.indexOf(removed);
            let valueIndex = back.indexOf(value);

            if (removedIndex !== valueIndex) return false;
        }
    }

    return stack.length === 0 ? true : false;

};