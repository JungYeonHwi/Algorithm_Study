function solution(prices) {
  var answer = [];

  for (let i = 0; i < prices.length - 1; i++) {
    let val = prices[i];
    let ans = 0;
    for (let j = i + 1; j < prices.length - 1; j++) {
      if (val <= prices[j]) {
        ans += 1;
      } else {
        break;
      }
    }
    answer.push(ans === 0 ? 1 : ans + 1);
  }

  answer.push(0);

  return answer;
}
