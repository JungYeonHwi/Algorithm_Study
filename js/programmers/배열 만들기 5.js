function solution(intStrs, k, s, l) {
  var answer = [];

  for (let i = 0; i < intStrs.length; i++) {
    let val = Number([...intStrs[i]].slice(s).slice(0, l).join(""));

    if (val > k) answer.push(val);
  }

  return answer;
}
