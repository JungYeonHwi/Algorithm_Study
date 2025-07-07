// 대문자인지 확인하는 함수 작성
function isUpperCase(str) {
  return str === str.toUpperCase();
}

// 소문자인지 확인하는 함수 작성
function isLowerCase(str) {
  return str === str.toLowerCase();
}

function solution(s) {
  var answer = "";
  let eo = [...s]
    .filter((item) => isUpperCase(item))
    .sort()
    .reverse();
  let th = [...s]
    .filter((item) => isLowerCase(item))
    .sort()
    .reverse();

  answer = th.join("") + eo.join("");

  return answer;
}
