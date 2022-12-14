function solution(array) {
  var answer = 0;

  for (let i = 0; i < array.length; i++) {
    let value = String(array[i]);
    for (let j = 0; j < value.length; j++) {
      if (value[j] == "7") {
        answer += 1;
      }
    }
  }

  return answer;
}
