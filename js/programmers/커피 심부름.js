function solution(order) {
  var answer = 0;

  for (let i = 0; i < order.length; i++) {
    if (order[i].includes("latte")) answer += 5000;
    else if (order[i].includes("mericano")) answer += 4500;
    else answer += 4500;
  }

  return answer;
}
