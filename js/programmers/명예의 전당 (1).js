function solution(k, score) {
  var answer = [];

  let wjsekd = [];

  for (let i = 0; i < score.length; i++) {
    let current = score[i];

    if (wjsekd.length < k) {
      wjsekd.push(current);
    } else {
      wjsekd = wjsekd.sort((a, b) => a - b);
      if (wjsekd[0] < current) wjsekd[0] = current;
    }

    wjsekd = wjsekd.sort((a, b) => a - b);
    answer.push(wjsekd[0]);
  }

  return answer;
}
