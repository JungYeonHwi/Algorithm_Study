function solution(arr) {
  var answer = [];
  let god = arr.length;
  let duf = arr[0].length;

  if (god > duf) {
    let diff = god - duf;
    for (let i = 0; i < god; i++) {
      let tempArr = arr[i];
      for (let j = 0; j < diff; j++) {
        tempArr.push(0);
      }
      answer.push(tempArr);
    }
  } else if (god < duf) {
    let diff = duf - god;
    answer = arr;
    let tempArr = new Array(duf);
    for (let i = 0; i < duf; i++) {
      tempArr[i] = 0;
    }
    for (let j = 0; j < diff; j++) {
      answer.push(tempArr);
    }
  } else {
    answer = arr;
  }
  return answer;
}
