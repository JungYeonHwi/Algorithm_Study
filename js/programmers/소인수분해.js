function isPrime(num) {
  if (num <= 1) {
    return false;
  }
  if (num % 2 === 0) {
    return num === 2 ? true : false;
  }

  const sqrt = parseInt(Math.sqrt(num));

  for (let divider = 3; divider <= sqrt; divider += 2) {
    if (num % divider === 0) {
      return false;
    }
  }

  return true;
}

function solution(n) {
  var answer = [];

  for (let i = 2; i <= n; i++) {
    if (n % i === 0 && isPrime(i)) answer.push(i);
  }

  return answer;
}
