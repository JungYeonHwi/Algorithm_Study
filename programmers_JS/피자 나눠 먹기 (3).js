function solution(slice, n) {
  var answer = 0;
  let value = 0;

  if (n % slice == 0) {
    value = 0;
  } else {
    value = 1;
  }

  answer = parseInt(n / slice) + value;

  return answer;
}
