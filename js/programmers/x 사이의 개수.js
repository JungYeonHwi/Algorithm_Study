function solution(myString) {
  var answer = myString.split("x").map((item) => item.length);
  return answer;
}
