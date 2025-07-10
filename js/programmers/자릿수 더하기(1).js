function solution(n) {
  var answer = [...String(n)].reduce((a, b) => parseInt(a) + parseInt(b));

  return Number(answer);
}
