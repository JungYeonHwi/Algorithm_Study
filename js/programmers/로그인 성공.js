function solution(id_pw, db) {
  var answer = "fail";
  let correct = 0;
  let wrong = 0;

  for (let i = 0; i < db.length; i++) {
    if (id_pw[0] === db[i][0] && id_pw[1] === db[i][1]) correct += 1;
    if (id_pw[0] === db[i][0] && id_pw[1] !== db[i][1]) wrong += 1;
  }

  if (correct === 1) return "login";
  if (wrong >= 1) return "wrong pw";

  return answer;
}
