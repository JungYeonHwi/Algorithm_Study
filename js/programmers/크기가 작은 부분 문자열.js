function solution(t, p) {
  var answer = 0;
  let s = String(t);

  for (let i = 0; i < s.length; i++) {
    let temp = "";
    for (let k = i; k < p.length + i; k++) {
      temp += s[k];
    }
    if (Number(temp) <= Number(p)) answer += 1;
    temp = "";
  }

  return answer;
}
