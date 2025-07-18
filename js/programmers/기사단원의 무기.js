function dirtn(num) {
  let result = [];
  let index = 1;
  while (index <= Math.sqrt(num)) {
    if (num % index === 0) {
      result.push(index);
      if (num / index !== index) result.push(num / index);
    }
    index++;
  }
  result.sort((a, b) => a - b);
  return result.length;
}

function solution(number, limit, power) {
  var answer = 0;

  let arr = [];
  for (let i = 1; i <= number; i++) {
    if (dirtn(i) > limit) arr.push(power);
    else arr.push(dirtn(i));
  }

  answer = arr.reduce((a, b) => a + b);

  return answer;
}
