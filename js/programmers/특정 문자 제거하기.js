function solution(my_string, letter) {
  var answer = "";

  for (let i = 0; i < my_string.length; i++) {
    if (my_string.charAt(i) != letter) {
      answer += my_string.charAt(i);
    }
  }

  return answer;
}
