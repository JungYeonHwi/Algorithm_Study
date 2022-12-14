function solution(numbers) {
  var answer = 0;

  let BruteForce = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i !== j) {
        BruteForce.push(numbers[i] * numbers[j]);
      }
    }
  }

  answer = Math.max(...BruteForce);

  return answer;
}
