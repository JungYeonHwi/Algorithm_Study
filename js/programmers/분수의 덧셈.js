let getGCD = (num1, num2) => {
  let gcd = 1;

  for (let i = 2; i <= Math.min(num1, num2); i++) {
    if (num1 % i === 0 && num2 % i === 0) gcd = i;
  }

  return gcd;
};

function solution(numer1, denom1, numer2, denom2) {
  var answer = [];

  let top = numer1 * denom2 + numer2 * denom1;
  let bottom = denom1 * denom2;

  let gcd = getGCD(top, bottom);

  answer = [top / gcd, bottom / gcd];

  return answer;
}
