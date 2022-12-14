function solution(array) {
  var answer = [];
  let value = Math.max(...array);

  answer.push(value);
  answer.push(array.indexOf(value));

  return answer;
}
