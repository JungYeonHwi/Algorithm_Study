function gkq(a, b) {
  if (!a && !b) return false;
  else return true;
}

function ry(a, b) {
  if (a && b) return true;
  else return false;
}

function solution(x1, x2, x3, x4) {
  var answer = ry(gkq(x1, x2), gkq(x3, x4));
  return answer;
}
