function solution(my_string, letter) {
  var answer = "";

  answer = [...my_string].filter((item) => item !== letter).join("");

  return answer;
}
