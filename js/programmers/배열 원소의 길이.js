function solution(strlist) {
  var answer = [];

  for (let i = 0; i < strlist.length; i++) {
    let data = strlist[i];
    answer.push(data.length);
  }

  return answer;
}
