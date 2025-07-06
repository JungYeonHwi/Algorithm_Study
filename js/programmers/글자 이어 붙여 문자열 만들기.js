function solution(my_string, index_list) {
  var answer = index_list.map((item) => my_string[item]).join("");
  return answer;
}
