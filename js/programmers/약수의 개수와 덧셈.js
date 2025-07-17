function dirtn(item) {
  let count = 0;
  for (let i = 1; i <= item; i++) {
    if (item % i === 0) count += 1;
  }

  return count;
}

function solution(left, right) {
  var answer = 0;

  for (let i = left; i < right + 1; i++) {
    if (dirtn(i) % 2 === 0) answer += i;
    else answer -= i;
  }

  return answer;
}
