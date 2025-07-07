function solution(a, b) {
  var result = "";
  var answer = 0;

  for (let i = 1; i < a; i++) {
    if (["1", "3", "5", "7", "8", "10"].includes(String(i))) answer += 31;
    else if (["4", "6", "9", "11"].includes(String(i))) answer += 30;
    else answer += 29;
  }

  answer += b;

  let val = answer % 7;
  let arr = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];

  result = arr[val];

  return result;
}
