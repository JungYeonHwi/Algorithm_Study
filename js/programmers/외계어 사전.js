function solution(spell, dic) {
  var answer = 2;

  let arr = [];

  dic.forEach(function (i) {
    let dicList = i.split("");
    let s = new Set();
    dicList.forEach(function (value) {
      s.add(value);
    });
    arr = [...s];

    arr.sort();
    spell.sort();

    if (arr.toString() == spell.toString()) {
      answer = 1;
    }
  });

  return answer;
}
