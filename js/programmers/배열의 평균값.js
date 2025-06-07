function solution(numbers) {
  var answer = 0;

  answer = numbers.reduce((a, b) => a + b) / numbers.length;

  return answer;
}
