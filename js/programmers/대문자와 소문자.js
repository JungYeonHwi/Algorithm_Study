// 대문자인지 확인하는 함수 작성
function isUpperCase(str) {
  return str === str.toUpperCase();
}

// 소문자인지 확인하는 함수 작성
function isLowerCase(str) {
  return str === str.toLowerCase();
}

function solution(my_string) {
  var answer = "";

  for (i = 0; i < my_string.length; i++) {
    if (isLowerCase(my_string[i])) {
      answer += my_string[i].toUpperCase();
    } else {
      answer += my_string[i].toLowerCase();
    }
  }

  return answer;
}
