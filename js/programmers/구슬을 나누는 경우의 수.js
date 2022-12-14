function solution(balls, share) {
  var answer = factorial(balls) / (factorial(balls - share) * factorial(share));
  return answer;
}

function factorial(num) {
  let answer = BigInt(1);
  for (let i = 2; i <= num; i++) {
    answer *= BigInt(i);
  }
  return answer;
}
