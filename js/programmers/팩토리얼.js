function solution(n) {
  var answer = 0;

  let value = 1;

  for (let i = 1; i < 10; i++) {
    value *= i;
    if (value <= n) {
      answer = i;
    }
  }

  return answer;
}
