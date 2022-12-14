function solution(n) {
  var answer = 2;

  for (let i = 1; i < parseInt(n / 2); i++) {
    if (i * i == n) {
      answer = 1;
    }
  }

  return answer;
}
