function solution(numbers, k) {
  var answer = 0;

  let len = numbers.length;

  answer = numbers[(2 * (k - 1)) % len];

  return answer;
}
