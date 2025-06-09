function solution(slice, n) {
  var answer = 0;

  answer = n % slice === 0 ? n / slice : Math.floor(n / slice) + 1;

  return answer;
}
