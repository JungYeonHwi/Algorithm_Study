function solution(my_string) {
  var answer = "";

  answer = [...my_string.toLowerCase()].sort().join("");

  return answer;
}
