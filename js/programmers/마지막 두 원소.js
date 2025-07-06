function solution(num_list) {
  var answer = num_list;
  let len = num_list.length;

  if (num_list[len - 1] > num_list[len - 2])
    answer.push(num_list[len - 1] - num_list[len - 2]);
  else answer.push(num_list[len - 1] * 2);

  return answer;
}
