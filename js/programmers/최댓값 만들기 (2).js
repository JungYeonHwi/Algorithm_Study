function solution(numbers) {
  var answer = 0;
  let len = numbers.length;

  numbers.sort((a, b) => a - b);

  return (answer = Math.max(
    numbers[0] * numbers[1],
    numbers[len - 1] * numbers[len - 2]
  ));
}
