function solution(my_strings, parts) {
  var answer = "";

  for (let i = 0; i < parts.length; i++) {
    let [a, b] = parts[i];

    let val = [...my_strings[i]].slice(a, b + 1).join("");
    answer += val;
  }

  return answer;
}
