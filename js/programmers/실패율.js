function solution(N, stages) {
  var answer = [];

  for (let i = 1; i <= N; i++) {
    let allPeople = stages.filter((item) => item >= i).length;
    let failPeople = stages.filter((item) => item === i).length;

    let val = failPeople / allPeople;

    answer.push([i, val]);
  }

  let result = [];

  answer.sort((a, b) => b[1] - a[1]);

  return answer.map((item) => item[0]);
}
