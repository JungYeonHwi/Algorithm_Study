function solution(spell, dic) {
  var answer = 2;

  for (let i = 0; i < dic.length; i++) {
    let item = dic[i].split("").sort().join("");
    let j = spell.sort().join("");

    if (item === j) return 1;
  }

  return answer;
}
