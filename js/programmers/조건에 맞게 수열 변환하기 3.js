function solution(arr, k) {
  var answer = [...arr];

  if (k % 2 === 0) answer = answer.map((item) => item + k);
  else answer = answer.map((item) => item * k);
  return answer;
}
