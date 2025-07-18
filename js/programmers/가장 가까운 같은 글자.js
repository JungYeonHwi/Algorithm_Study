function solution(s) {
  var answer = [];
  let used = [];

  for (let i = 0; i < s.length; i++) {
    let current = s[i];
    if (!used.includes(current)) {
      answer.push(-1);
      used.push(current);
    } else {
      let temp = s.slice(0, i);
      let index = temp.lastIndexOf(current);
      answer.push(i - index);
    }
  }

  return answer;
}
