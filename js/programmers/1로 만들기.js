function solution(num_list) {
  var answer = 0;

  for (let i = 0; i < num_list.length; i++) {
    let val = num_list[i];
    while (val !== 1) {
      if (val % 2 === 0) {
        val = val / 2;
        answer += 1;
      } else {
        val = val - 1;
        val = val / 2;
        answer += 1;
      }
    }
  }

  return answer;
}
