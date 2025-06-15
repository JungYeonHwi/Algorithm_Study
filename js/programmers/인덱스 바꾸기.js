function solution(my_string, num1, num2) {
  var answer = [...my_string]
    .map((item, index) => {
      if (index === num1) return my_string[num2];
      else if (index === num2) return my_string[num1];
      else return item;
    })
    .join("");
  return answer;
}
