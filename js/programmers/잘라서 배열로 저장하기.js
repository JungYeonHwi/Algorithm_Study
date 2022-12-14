function solution(my_str, n) {
  var answer = [];

  for (let i = 0; i < my_str.length / n; i++) {
    let part = "";
    for (let j = i * n; j < i * n + n; j++) {
      if (my_str[j]) {
        part += my_str[j];
      } else break;
    }
    answer.push(part);
  }

  return answer;
}
