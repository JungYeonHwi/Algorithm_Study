function solution(my_string) {
  var answer = "";

  for (let i = 0; i < my_string.length; i++) {
    if (my_string.indexOf(my_string[i]) === i) {
      answer += my_string[i];
    }
  }

  return answer;
}
