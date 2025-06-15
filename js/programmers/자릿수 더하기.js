function solution(n) {
  if (n === 0) return 0;
  var answer = [...n.toString()].reduce((a, b) => Number(a) + Number(b));
  return answer;
}
