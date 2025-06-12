function solution(sides) {
  var answer = 0;
  let arr = [];

  let max = Math.max(...sides);
  let min = Math.min(...sides);

  // 가장 긴 변이 max인 경우
  for (let i = 0; i <= max; i++) {
    if (i + min > max) arr.push(i);
  }

  // 가장 긴 변이 알수 없는 경우
  for (let i = max; i < max + min; i++) {
    arr.push(i);
  }

  answer = new Set(arr).size;

  return answer;
}
