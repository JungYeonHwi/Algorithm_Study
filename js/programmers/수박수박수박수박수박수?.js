function solution(n) {
  var answer = "수박".repeat(Number(n / 2));

  answer += n % 2 !== 0 ? "수" : "";

  return answer;
}
