function solution(n) {
  var answer = n + 1;

  let c = n.toString(2).match(/1/g).length;

  while (answer) {
    let s = answer.toString(2).match(/1/g).length;

    if (c === s) return answer;
    else answer += 1;
  }

  return answer;
}
