function solution(n) {
  var answer = 0;

  let ghf = 0;
  let wkr = 0;

  for (let i = 0; i <= n; i++) {
    if (i % 2 === 0) wkr += i * i;
    else ghf += i;
  }

  answer = n % 2 === 0 ? wkr : ghf;

  return answer;
}
