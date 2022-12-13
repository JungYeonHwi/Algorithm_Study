function solution(denum1, num1, denum2, num2) {
  var answer = [];

  let a = num1;
  let b = num2;

  while (a % b !== 0) {
    let r = a % b;

    if (r !== 0) {
      a = b;
      b = r;
    }
  }

  let min = (num1 * num2) / b;

  let quotient1 = min / num1;
  let quotient2 = min / num2;

  let newdenum1 = quotient1 * denum1;
  let newdenum2 = quotient2 * denum2;

  let newdenum = newdenum1 + newdenum2;

  a = min;
  b = newdenum;

  while (a % b !== 0) {
    let r = a % b;

    if (r !== 0) {
      a = b;
      b = r;
    }
  }

  let numerator = newdenum / b;
  let denominator = min / b;

  answer.push(numerator);
  answer.push(denominator);

  return answer;
}
