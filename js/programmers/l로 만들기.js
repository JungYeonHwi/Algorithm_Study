function solution(myString) {
  var answer = "";

  let arr = [...myString];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < "l") {
      answer += "l";
    } else {
      answer += arr[i];
    }
  }

  return answer;
}
