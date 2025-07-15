function solution(board, moves) {
  var answer = 0;
  let arr = [];

  for (let i = 0; i < board.length; i++) {
    let temp = [];
    for (let j = 0; j < board.length; j++) {
      if (board[j][i] === 0) continue;
      else temp.push(board[j][i]);
    }
    arr.push(temp.reverse());
  }

  let ans = [];

  for (let i = 0; i < moves.length; i++) {
    let find = arr[moves[i] - 1];
    let len = arr[moves[i] - 1].length;
    let val = find[len - 1];

    if (val) {
      if (ans[ans.length - 1] === val) {
        answer += 2;
        ans.pop();
      } else {
        ans.push(val);
      }
    }

    find.pop();
  }

  return answer;
}
