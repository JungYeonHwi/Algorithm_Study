function solution(brown, yellow) {
  var answer = [];

  if (yellow === 1) return [3, 3];
  if (yellow === 2) return [4, 3];

  for (let i = 1; i < yellow; i++) {
    if (yellow % i === 0) {
      let rkfh = i;
      let tpfh = yellow / rkfh;

      if (rkfh * 2 + tpfh * 2 + 4 === brown) return [tpfh + 2, rkfh + 2];
    }
  }

  return answer;
}
