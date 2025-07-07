function solution(s) {
  var answer = parseInt(s);
  if ((s.length === 4 || s.length === 6) && answer == s) {
    if (Number.isInteger(answer) === true) return true;
  }
  return false;
}
