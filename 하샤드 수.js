function solution(x) {
  var answer = x % [...String(x)].reduce((a, b) => Number(a) + Number(b)) === 0;
  return answer;
}
