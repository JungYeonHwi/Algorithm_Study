function solution(numbers) {
  var answer = 45;
  let n = numbers.reduce((a, b) => a + b);

  return answer - n;
}
