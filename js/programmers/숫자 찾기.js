function solution(num, k) {
  let ind = ("" + num).indexOf(k);
  return ind === -1 ? -1 : ind + 1;
}
