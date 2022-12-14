function solution(board) {
  let answer = 0;
  // 전체 순회
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      // board[i][j]의 값이 1인경우 상하좌우 및 대각선 검사를 실행
      if (board[i][j] === 1) {
        // 상하 좌우를 2로 변경하되 이는 해당 칸이 0인 경우에만 해당 즉 폭탄은 건들지 않는다.
        // 맨 윗줄이 아닌 경우
        if (i !== 0 && board[i - 1][j] !== 1) {
          board[i - 1][j] = 2;
        }
        // 맨 아랫줄이 아닌 경우
        if (i !== board.length - 1 && board[i + 1][j] !== 1) {
          board[i + 1][j] = 2;
        }
        // 맨 왼쪽이 아닌 경우
        if (j !== 0 && board[i][j - 1] !== 1) {
          board[i][j - 1] = 2;
        }
        // 맨 오른쪽이 아닌 경우
        if (j !== board[i].length - 1 && board[i][j + 1] !== 1) {
          board[i][j + 1] = 2;
        }
        // 맨 대각선 윗 왼쪽이 아닌 경우
        if (i !== 0 && j !== 0 && board[i - 1][j - 1] !== 1) {
          board[i - 1][j - 1] = 2;
        }
        // 맨 대각선 윗 오른쪽이 아닌 경우
        if (i !== 0 && j !== board[i].length - 1 && board[i - 1][j + 1] !== 1) {
          board[i - 1][j + 1] = 2;
        }
        // 맨 대각선 아랫 왼쪽이 아닌 경우
        if (i !== board.length - 1 && j !== 0 && board[i + 1][j - 1] !== 1) {
          board[i + 1][j - 1] = 2;
        }
        // 맨 대각선 아랫 오른쪽이 아닌 경우
        if (
          i !== board.length - 1 &&
          j !== board[i].length - 1 &&
          board[i + 1][j + 1] !== 1
        ) {
          board[i + 1][j + 1] = 2;
        }
      }
    }
  }
  board.forEach((a) => a.forEach((b) => (b === 0 ? answer++ : null)));
  return answer;
}
