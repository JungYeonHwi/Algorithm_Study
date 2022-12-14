function solution(my_string, num1, num2) {
  var answer = "";

  let strList = my_string.split("");

  let value = strList[num1];

  strList[num1] = strList[num2];
  strList[num2] = value;

  for (let i = 0; i < strList.length; i++) {
    answer += strList[i];
  }

  return answer;
}
