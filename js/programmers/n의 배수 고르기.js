function solution(n, numlist) {
  var answer = numlist.filter((item) => item % n === 0 && item);
  return answer;
}
