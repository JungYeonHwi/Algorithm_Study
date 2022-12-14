function solution(rsp) {
  var answer = "";

  let rspList = rsp.split("");

  for (let i = 0; i < rspList.length; i++) {
    if (rspList[i] == "2") {
      answer += "0";
    } else if (rspList[i] == "0") {
      answer += "5";
    } else if (rspList[i] == "5") {
      answer += "2";
    }
  }

  return answer;
}
