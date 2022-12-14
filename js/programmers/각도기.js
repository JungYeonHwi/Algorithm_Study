function solution(angle) {
  var answer = 0;

  if (angle == 90) {
    answer = 2;
  } else if (angle == 180) {
    answer = 4;
  } else if (0 < angle && angle < 90) {
    answer = 1;
  } else if (90 < angle && angle < 180) {
    answer = 3;
  }

  return answer;
}
