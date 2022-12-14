function solution(num, k) {
  var answer = -1;

  let numStr = String(num).slice();

  for (let i = 0; i < numStr.length; i++) {
    if (k == Number(numStr.charAt(i))) {
      answer = i + 1;
      break;
    }
  }

  return answer;
}
