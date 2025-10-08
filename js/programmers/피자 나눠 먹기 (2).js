function solution(n) {
  var answer = 0;

  if (n % 6 === 0) return n / 6;

  for (let k = 1; k < 600; k++) {
    if ((k * 6) % n === 0) {
      return k;
    }
  }

  return answer;
}
