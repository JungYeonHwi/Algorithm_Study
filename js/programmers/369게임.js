function solution(order) {
  var answer = 0;

  strOrder = String(order);

  for (let i = 0; i < strOrder.length; i++) {
    let data = strOrder.charAt(i);

    if ("3" == data) {
      answer += 1;
    } else if ("6" == data) {
      answer += 1;
    } else if ("9" == data) {
      answer += 1;
    }
  }

  return answer;
}
