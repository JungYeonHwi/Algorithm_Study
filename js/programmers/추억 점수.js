function solution(name, yearning, photo) {
  var answer = [];

  for (let i = 0; i < photo.length; i++) {
    let s = 0;
    for (let j = 0; j < photo[i].length; j++) {
      let current = photo[i][j];
      let index = name.indexOf(current);

      if (index !== -1) s += yearning[index];
    }
    answer.push(s);
  }

  return answer;
}
