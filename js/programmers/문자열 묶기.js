function solution(strArr) {
  var answer = 0;
  let s = strArr.map((item) => item.length);
  let m = Math.max(...s);
  let arr = new Array(m + 1).fill(0);
  s.map((item) => (arr[item] += 1));
  return (answer = Math.max(...arr));
}
