function solution(k, m, score) {
  var answer = 0;

  score = score.sort((a, b) => b - a);
  let arr = [];

  for (let i = 0; i < score.length; i += m) {
    let temp = [];
    for (let k = i; k < m + i; k++) {
      if (score[k]) {
        temp.push(score[k]);
      } else {
        temp.push(0);
      }
    }
    arr.push(temp);
  }

  for (let i = 0; i < arr.length; i++) {
    let temp = arr[i];
    temp = temp.sort((a, b) => a - b);
    let value = temp[0] * m;
    answer += value;
  }

  return answer;
}
