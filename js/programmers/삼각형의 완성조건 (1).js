function solution(sides) {
  var answer = 0;

  sides.sort((a, b) => b - a);

  answer = sides[0] < sides[1] + sides[2] ? 1 : 2;

  return answer;
}
