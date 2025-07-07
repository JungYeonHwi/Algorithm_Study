function solution(a, b) {
  var answer = 0;

  let m1 = Math.max(a, b);
  let m2 = Math.min(a, b);

  for (let i = m2; i <= m1; i++) {
    answer += i;
  }

  return answer;
}
