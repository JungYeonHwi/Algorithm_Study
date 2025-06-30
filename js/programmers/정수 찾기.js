function solution(num_list, n) {
  var answer = 0;

  let s = num_list.filter((item) => item === n);
  answer = s.length > 0 ? 1 : 0;

  return answer;
}
