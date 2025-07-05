function solution(my_string, indices) {
  var answer = [...my_string]
    .filter((item, index) => !indices.includes(index))
    .join("");
  return answer;
}
