function solution(arr, n) {
  var answer = [];
  if (arr.length % 2 === 0)
    answer = arr.map((item, index) => (index % 2 === 0 ? item : item + n));
  else answer = arr.map((item, index) => (index % 2 === 0 ? item + n : item));
  return answer;
}
