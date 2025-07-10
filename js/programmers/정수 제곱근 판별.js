function solution(n) {
  let val = Math.sqrt(n);

  var answer = Number.isInteger(val) ? Math.pow(val + 1, 2) : -1;
  return answer;
}
