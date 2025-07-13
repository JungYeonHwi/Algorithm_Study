function solution(num) {
  var answer = 0;

  if (num === 1) return 0;

  for (let count = 0; count < 500; count++) {
    if (num === 1) return count;
    else {
      if (num % 2 === 0) num = num / 2;
      else num = num * 3 + 1;
    }
  }

  return -1;
}
