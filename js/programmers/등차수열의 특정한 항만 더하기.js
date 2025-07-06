function solution(a, d, included) {
  var answer = 0;

  let arr = [a];

  for (let i = 1; i < included.length; i++) {
    arr.push(arr[arr.length - 1] + d);
  }

  let filteredArr = arr.filter((item, index) => included[index]);
  answer = filteredArr.reduce((a, b) => a + b);

  return answer;
}
