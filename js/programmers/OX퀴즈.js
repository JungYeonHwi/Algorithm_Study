function solution(quiz) {
  var answer = [];

  for (i = 0; i < quiz.length; i++) {
    let arr = [...quiz[i].split(" ")];
    let ans = 0;
    if (arr[1] === "+") ans = Number(arr[0]) + Number(arr[2]);
    else ans = Number(arr[0]) - Number(arr[2]);

    ans.toString() === arr[4] ? answer.push("O") : answer.push("X");
  }

  return answer;
}
