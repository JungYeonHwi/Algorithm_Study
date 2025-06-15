function solution(my_string) {
  var answer = "";

  let set = new Set([...my_string]);
  answer = [...set].join("");

  return answer;
}
