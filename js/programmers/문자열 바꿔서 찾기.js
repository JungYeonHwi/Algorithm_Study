function solution(myString, pat) {
  var answer = 0;

  let str = "";
  for (let i = 0; i < myString.length; i++) {
    if (myString[i] === "A") str += "B";
    else str += "A";
  }

  answer = str.includes(pat) ? 1 : 0;

  return answer;
}
