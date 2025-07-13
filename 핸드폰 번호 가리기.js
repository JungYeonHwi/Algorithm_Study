function solution(phone_number) {
  var answer = "";
  let len = phone_number.length - 5;

  for (let i = 0; i < phone_number.length; i++) {
    if (i <= len) answer += "*";
    else answer += phone_number[i];
  }

  return answer;
}
