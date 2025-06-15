function solution(array) {
  var answer = 0;

  for (i = 0; i < array.length; i++) {
    let arr = [...array[i].toString()];
    answer += arr.filter((item) => item === "7").length;
  }

  return answer;
}
