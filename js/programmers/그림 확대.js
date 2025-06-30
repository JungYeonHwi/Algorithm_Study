function solution(picture, k) {
  var answer = [];
  for (let i = 0; i < picture.length; i++) {
    let arr = [...picture[i]];
    let temp = [];
    for (let a = 0; a < arr.length; a++) {
      for (let j = 0; j < k; j++) {
        temp.push(arr[a]);
      }
    }
    for (let b = 0; b < k; b++) {
      answer.push(temp.join(""));
    }
  }
  return answer;
}
