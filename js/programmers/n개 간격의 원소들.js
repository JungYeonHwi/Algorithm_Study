function solution(num_list, n) {
  var answer = num_list.filter((item, index) => index % n === 0);
  return answer;
}
