function solution(date1, date2) {
  var answer = 0;

  if (new Date(date1) < new Date(date2)) answer = 1;
  else answer = 0;

  return answer;
}
