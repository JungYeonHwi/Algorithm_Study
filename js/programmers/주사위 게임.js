function solution(a, b) {
  var answer = 0;

  if (a % 2 !== 0 && b % 2 !== 0) answer = a * a + b * b;
  else if (a % 2 === 0 && b % 2 === 0) answer = Math.abs(a - b);
  else answer = 2 * (a + b);

  return answer;
}
