function solution(dots) {
  var answer = 0;

  dots.sort((a, b) => a[0] - b[0]);

  let oneSide = Math.abs(dots[0][1] - dots[1][1]);
  let otherSide = Math.abs(dots[0][0] - dots[2][0]);

  answer = oneSide * otherSide;

  return answer;
}
