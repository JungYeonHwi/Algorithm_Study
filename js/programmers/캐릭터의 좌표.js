function solution(keyinput, board) {
  var answer = [0, 0];

  keyinput.forEach(function (i) {
    let value = 0;

    if (i == "left") {
      value = answer[0] - 1;
      if (Math.abs(value) <= parseInt((board[0] - 1) / 2)) {
        answer[0] -= 1;
      }
    }
    if (i == "right") {
      value = answer[0] + 1;
      if (Math.abs(value) <= parseInt((board[0] - 1) / 2)) {
        answer[0] += 1;
      }
    }
    if (i == "up") {
      value = answer[1] + 1;
      if (Math.abs(value) <= parseInt((board[1] - 1) / 2)) {
        answer[1] += 1;
      }
    }
    if (i == "down") {
      value = answer[1] - 1;
      if (Math.abs(value) <= parseInt((board[1] - 1) / 2)) {
        answer[1] -= 1;
      }
    }
  });

  return answer;
}
