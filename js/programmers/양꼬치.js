function solution(n, k) {
  var answer = 0;

  let nSum = n * 12000;
  let kSum = k * 2000;
  answer = nSum + kSum;

  let bonus = parseInt(n / 10);
  answer = nSum + kSum - bonus * 2000;

  return answer;
}
