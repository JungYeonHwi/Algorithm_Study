function solution(i, j, k) {
  var answer = 0;

  for (index = i; index <= j; index++) {
    let arr = [...index.toString()];

    answer += arr.filter((item) => item === k.toString()).length;
  }

  return answer;
}
