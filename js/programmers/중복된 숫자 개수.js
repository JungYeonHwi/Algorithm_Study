function solution(array, n) {
  var answer = 0;

  let filteredArray = array.filter((item) => item === n);

  answer = filteredArray.length;

  return answer;
}
