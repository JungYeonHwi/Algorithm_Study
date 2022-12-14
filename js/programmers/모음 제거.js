function solution(my_string) {
  var answer = "";

  for (let i = 0; i < my_string.length; i++) {
    let value = my_string.charAt(i);
    if (
      value != "a" &&
      value != "e" &&
      value != "i" &&
      value != "o" &&
      value != "u"
    ) {
      answer += value;
    }
  }

  return answer;
}
