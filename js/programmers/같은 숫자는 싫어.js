function solution(arr) {
  var answer = [];

  if (arr.length === 1) answer = arr;
  else {
    let temp = arr[0];

    for (let i = 1; i < arr.length; i++) {
      if (temp === arr[i]) continue;
      else {
        answer.push(temp);
        temp = arr[i];
      }
    }

    if (temp === arr[arr.length - 1]) answer.push(temp);
  }

  return answer;
}
