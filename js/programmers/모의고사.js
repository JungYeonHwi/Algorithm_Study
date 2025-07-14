function findAllIndexes(arr, val) {
  const indexes = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === val) {
      indexes.push(i + 1);
    }
  }
  return indexes;
}

function solution(answers) {
  var answer = [0, 0, 0];

  let one = [1, 2, 3, 4, 5];
  let two = [2, 1, 2, 3, 2, 4, 2, 5];
  let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === one[i % 5]) answer[0] += 1;
    if (answers[i] === two[i % 8]) answer[1] += 1;
    if (answers[i] === three[i % 10]) answer[2] += 1;
  }

  let maxValue = Math.max(...answer);
  let result = findAllIndexes(answer, maxValue);

  return result;
}
