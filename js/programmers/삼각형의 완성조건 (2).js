function solution(sides) {
  var answer = 0;

  let M = Math.max(...sides);
  let m = Math.min(...sides);

  // M이 가장 긴 변인 경우

  for (let i = 1; i < M + 1; i++) {
    if (i + m > M) {
      answer += 1;
    }
  }

  // 나머지 한 변이 가장 긴 변인 경우
  let value = M + 1;
  while (value < M + m) {
    answer += 1;
    value += 1;
  }

  return answer;
}
