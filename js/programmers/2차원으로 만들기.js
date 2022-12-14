function solution(num_list, n) {
  var answer = [];

  let cnt = 0;
  let value = [];

  for (let i = 0; i < num_list.length; i++) {
    cnt += 1;
    value.push(num_list[i]);

    if (cnt == n) {
      answer.push(value);
      value = [];
      cnt = 0;
    } else {
      continue;
    }
  }

  return answer;
}
