function solution(numbers) {
  var answer = 0;

  let sum = numbers.reduce((a, b) => a + b, 0);

  answer = sum / numbers.length;

  return answer;
}
