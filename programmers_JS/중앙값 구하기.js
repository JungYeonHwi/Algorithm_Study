function solution(array) {
  var answer = 0;

  array = array.sort((a, b) => a - b);

  let idx = Math.floor(array.length / 2);
  answer = array[idx];

  return answer;
}
