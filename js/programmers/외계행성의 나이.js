function solution(age) {
  var answer = "";

  var value = String(age);

  let arr = value.split("");

  for (let i = 0; i < arr.length; i++) {
    let data = arr[i];

    if (data == "0") {
      answer += "a";
    } else if (data == "1") {
      answer += "b";
    } else if (data == "2") {
      answer += "c";
    } else if (data == "3") {
      answer += "d";
    } else if (data == "4") {
      answer += "e";
    } else if (data == "5") {
      answer += "f";
    } else if (data == "6") {
      answer += "g";
    } else if (data == "7") {
      answer += "h";
    } else if (data == "8") {
      answer += "i";
    } else if (data == "9") {
      answer += "j";
    }
  }

  return answer;
}
