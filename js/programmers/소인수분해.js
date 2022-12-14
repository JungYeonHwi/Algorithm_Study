function solution(n) {
  var answer = [];

  let result = [];
  let divisor = 2;

  while (n >= 2) {
    if (n % divisor === 0) {
      result.push(divisor);
      n = n / divisor;
    } else divisor++;
  }

  answer = [...new Set(result)];
  return answer;
}
