function solution(num_str) {
  var answer = 0;
  answer = [...num_str].map((item) => (answer += Number(item)));
  return answer[num_str.length - 1];
}
