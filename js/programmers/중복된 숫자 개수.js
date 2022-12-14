function solution(array, n) {
  var answer = 0;

  array.forEach(function (i) {
    if (i == n) {
      answer += 1;
    }
  });

  return answer;
}
