function solution(array, height) {
  var answer = 0;

  let filteredArray = array.filter((item) => item > height);

  answer = filteredArray.length;

  return answer;
}
