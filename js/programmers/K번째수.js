function solution(array, commands) {
  var answer = [];

  for (let index = 0; index < commands.length; index++) {
    let [i, j, k] = commands[index];

    let arr = array.slice(i - 1, j).sort((a, b) => a - b);
    answer.push(arr[k - 1]);
  }

  return answer;
}
