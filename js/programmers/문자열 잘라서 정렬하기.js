function solution(myString) {
  var answer = myString
    .split("x")
    .filter((item) => item !== "")
    .sort();

  return answer;
}
