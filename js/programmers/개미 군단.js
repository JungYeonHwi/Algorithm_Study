function solution(hp) {
  var answer = 0;

  let first = parseInt(hp / 5);
  let second = parseInt((hp - first * 5) / 3);
  let third = hp - first * 5 - second * 3;
  answer = first + second + third;

  return answer;
}
