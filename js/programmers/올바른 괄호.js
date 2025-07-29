function solution(s) {
  var answer = true;
  let stack = [];

  for (let i = 0; i < s.length; i++) {
    let item = s[i];
    if (item === "(") stack.push("(");
    else {
      if (stack.length === 0) return false;
      else stack.pop();
    }
  }

  return (answer = stack.length === 0 ? true : false);
}
