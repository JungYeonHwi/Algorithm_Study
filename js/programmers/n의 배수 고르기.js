function solution(n, numlist) {
  var answer = [];

  numlist.forEach(function (value) {
    if (value % n == 0) {
      answer.push(value);
    }
  });

  return answer;
}
