function solution(n) {
  var answer = [...String(n)].reverse().map((item) => Number(item));
  return answer;
}
