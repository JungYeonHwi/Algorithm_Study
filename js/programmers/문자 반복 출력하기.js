function solution(my_string, n) {
  var answer = "";
  for (i = 0; i < my_string.length; i++) {
    for (t = 0; t < n; t++) {
      answer += my_string[i];
    }
  }
  return answer;
}
