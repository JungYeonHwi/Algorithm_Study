/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let arr = s.split("");

  let stack = [];
  let chk = 1;

  if (s.length == 1) {
    return false;
  }

  arr.forEach(function (i) {
    if (i == "(" || i == "{" || i == "[") {
      stack.push(i);
    } else {
      if (stack.length == 0) {
        chk = 0;
      } else {
        let value = stack.pop();

        if (i == ")" && value != "(") {
          chk = 0;
        } else if (i == "}" && value != "{") {
          chk = 0;
        } else if (i == "]" && value != "[") {
          console.log(123);
          chk = 0;
        }
      }
    }
  });

  if (stack.length == 0 && chk) {
    return true;
  } else {
    return false;
  }
};
