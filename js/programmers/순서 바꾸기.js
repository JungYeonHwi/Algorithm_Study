function solution(num_list, n) {
  var answer = [];
  var after = num_list.slice(n, num_list.length);
  var before = num_list.slice(0, n);

  answer = after.concat(before);
  return answer;
}
