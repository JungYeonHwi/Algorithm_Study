function solution(number) {
  var answer = [...String(number)].reduce((a, b) => Number(a) + Number(b)) % 9;
  return answer;
}
