function solution(my_string, s, e) {
  var answer = "";

  for (let i = 0; i < s; i++) {
    answer += my_string[i];
  }

  for (let i = e; i >= s; i--) {
    answer += my_string[i];
  }

  for (let i = (e += 1); i < my_string.length; i++) {
    answer += my_string[i];
  }

  return answer;
}
