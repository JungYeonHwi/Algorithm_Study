function solution(arr) {
  var answer = arr.reduce((a, b) => a + b) / arr.length;
  return answer;
}
