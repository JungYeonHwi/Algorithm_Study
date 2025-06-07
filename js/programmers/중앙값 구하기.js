function solution(array) {
  var answer = 0;

  let filteredArray = array.sort((a, b) => a - b);

  answer = filteredArray[(array.length - 1) / 2];

  return answer;
}
