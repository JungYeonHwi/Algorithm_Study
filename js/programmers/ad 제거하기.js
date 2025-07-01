function solution(strArr) {
  var answer = strArr.filter((item) => !item.includes("ad"));
  return answer;
}
