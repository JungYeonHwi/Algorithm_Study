function solution(numbers) {
  var answer = 0;

  numbers.sort(function (a, b) {
    return a - b;
  });

  answer = numbers[numbers.length - 1] * numbers[numbers.length - 2];

  return answer;
}
