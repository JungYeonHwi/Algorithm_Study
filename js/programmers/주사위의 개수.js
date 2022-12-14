function solution(box, n) {
  var answer =
    parseInt(box[0] / n) * parseInt(box[1] / n) * parseInt(box[2] / n);
  return answer;
}
