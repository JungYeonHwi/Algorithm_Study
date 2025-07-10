function solution(n) {
  var answer = Number([...String(n)].sort().reverse().join(""));
  return answer;
}
