function solution(dots) {
  var answer = 0;

  let x = [];
  let y = [];

  x = dots.map((item) => item[0]);
  y = dots.map((item) => item[1]);

  let xx = new Set(x);
  let yy = new Set(y);

  let xxx = [...xx].sort((a, b) => a - b);
  let yyy = [...yy].sort((a, b) => a - b);

  answer = (xxx[1] - xxx[0]) * (yyy[1] - yyy[0]);

  return answer;
}
