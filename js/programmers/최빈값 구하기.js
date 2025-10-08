function solution(array) {
  var answer = 0;

  let m = Math.max(...array);
  let arr = new Array(m + 1).fill(0);

  for (let i = 0; i < array.length; i++) {
    arr[array[i]] += 1;
  }

  let val = Math.max(...arr);

  for (let i = 0; i < arr.length; i++) {
    if (val === arr[i]) {
      if (answer === 0) answer = i;
      else return -1;
    }
  }

  return answer;
}
