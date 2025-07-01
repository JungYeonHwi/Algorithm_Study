function solution(my_string) {
  var answer = [...my_string.split(" ")].filter((item) => item !== "");
  return answer;
}
