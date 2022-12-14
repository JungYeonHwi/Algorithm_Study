function solution(str1, str2) {
  var answer = 0;

  let idx = str1.indexOf(str2);

  if (idx == -1) {
    answer = 2;
  } else {
    answer = 1;
  }

  return answer;
}
