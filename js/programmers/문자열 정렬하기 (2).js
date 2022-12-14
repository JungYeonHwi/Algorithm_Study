function solution(my_string) {
  var answer = "";

  lowerString = my_string.toLowerCase();
  strList = lowerString.split("");

  strList.sort().forEach(function (value) {
    answer += value;
  });

  return answer;
}
