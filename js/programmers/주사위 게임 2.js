function solution(a, b, c) {
  let sum1 = a + b + c;
  let sum2 = a * a + b * b + c * c;
  let sum3 = a ** 3 + b ** 3 + c ** 3;

  if (a === b && b === c) return sum1 * sum2 * sum3;
  else if (a === b || a === c || b === c) return sum1 * sum2;
  else return sum1;
}
