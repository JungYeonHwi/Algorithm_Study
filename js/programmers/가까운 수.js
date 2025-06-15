function solution(array, n) {
  var answer = 0;

  array = array.sort((a, b) => a - b);

  let arr = array.map((item) => [item, Math.abs(item - n)]);
  arr.sort((a, b) => a[1] - b[1]);

  answer = arr[0][0];

  return answer;
}
