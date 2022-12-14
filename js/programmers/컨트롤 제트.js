function solution(s) {
  var answer = 0;

  let stack = [];

  let arr = s.split(" ");

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "Z") {
      if (arr[i - 1]) {
        arr.splice(i - 1, 2);
        i -= 2;
      } else {
        arr.splice(i, 1);
        i--;
      }
    }
  }

  answer = arr.reduce((a, b) => a * 1 + b * 1, 0);

  return answer;
}
