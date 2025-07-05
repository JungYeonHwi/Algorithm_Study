function solution(arr) {
  var answer = [];

  if (!arr.includes(2)) answer = [-1];
  else {
    const startIdx = arr.indexOf(2);
    const endIdx = arr.lastIndexOf(2);

    answer = arr.slice(startIdx, endIdx + 1);
  }

  return answer;
}
