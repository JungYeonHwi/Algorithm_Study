function solution(n) {
  var answer = 0;

  for (let i = n; i > 1; i--) {
    if (n % i === 1) answer = i;
  }

  return answer;
}
