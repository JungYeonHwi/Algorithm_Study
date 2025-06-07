function solution(n) {
  var answer = [];
  let arr = [];

  for (i = 0; i < n + 1; i++) {
    arr.push(i);
  }

  let newArr = arr.filter((item) => item % 2 !== 0);

  answer = newArr.sort((a, b) => a - b);

  return answer;
}
