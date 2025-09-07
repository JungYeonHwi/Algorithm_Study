/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = [];

  if (s.length === 1) return false;

  let arr = ["(", "{", "["];

  for (let i = 0; i < s.length; i++) {
    if (arr.includes(s[i])) stack.push(s[i]);
    else {
      let popItem = stack.pop();
      if (s[i] === ")" && popItem === "(") continue;
      if (s[i] === "}" && popItem === "{") continue;
      if (s[i] === "]" && popItem === "[") continue;

      return false;
    }
  }

  if (stack.length !== 0) return false;
  else return true;
};
