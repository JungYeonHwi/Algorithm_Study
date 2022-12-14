function solution(my_string) {
  var answer = my_string
    .match(/[0-9]/g)
    .map((str) => parseInt(str))
    .sort((a, b) => a - b);

  return answer;
}
