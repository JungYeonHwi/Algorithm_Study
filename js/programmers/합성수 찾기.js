function solution(n) {
  var answer = 0;

  if (n == 1) {
    answer = 0;
  } else {
    for (let i = 2; i < n + 1; i++) {
      let cnt = 0;
      for (let j = 2; j < i + 1; j++) {
        if (i % j == 0) {
          cnt += 1;
        }
      }
      if (cnt > 1) {
        answer += 1;
      }
    }
  }

  return answer;
}
