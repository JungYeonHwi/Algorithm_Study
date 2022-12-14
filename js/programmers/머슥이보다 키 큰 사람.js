function solution(array, height) {
  var answer = 0;

  array.forEach(function (i) {
    if (i > height) {
      answer += 1;
    }
  });

  return answer;
}
