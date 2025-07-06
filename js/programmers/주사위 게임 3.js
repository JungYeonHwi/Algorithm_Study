function solution(a, b, c, d) {
  var answer = 0;
  var set = new Set([a, b, c, d]);
  var temp = [a, b, c, d].sort((a, b) => a - b);

  if (set.size == 1) {
    answer = 1111 * a;
  } else if (set.size == 2) {
    if (temp[0] == temp[1] && temp[2] == temp[3]) {
      answer = (temp[0] + temp[2]) * Math.abs(temp[0] - temp[2]);
    } else {
      answer =
        temp[0] == temp[1] && temp[1] == temp[2]
          ? Math.pow(10 * temp[0] + temp[3], 2)
          : Math.pow(10 * temp[3] + temp[0], 2);
    }
  } else if (set.size == 3) {
    answer =
      temp[0] == temp[1]
        ? temp[2] * temp[3]
        : temp[1] == temp[2]
        ? temp[0] * temp[3]
        : temp[0] * temp[1];
  } else {
    answer = temp[0];
  }

  return answer;
}
