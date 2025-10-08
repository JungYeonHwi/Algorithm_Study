function isPrime(n) {
  for (let i = 2; i < Math.sqrt(n) + 1; i++) {
    if (n % i === 0) return true;
  }

  return false;
}

function solution(n) {
  var answer = 0;

  if (n === 1) return 0;
  if (n === 2) return 0;

  for (let i = 3; i <= n; i++) {
    if (isPrime(i)) answer += 1;
  }

  return answer;
}
