function solution(my_string) {
  var answer = 0;

  var answer = my_string
    .match(/[0-9]/g)
    .map((str) => parseInt(str))
    .reduce((accumulator, current) => accumulator + current, 0);

  return answer;
}
