function solution(my_string, queries) {
  var answer = my_string.split("");

  let result = "";

  for (let x of queries) {
    let num = x[1] - x[0];
    result = answer.slice(x[0], x[1] + 1).reverse();

    answer.splice(x[0], num + 1);
    answer.splice(x[0], 0, ...result);
  }

  return answer.join("");
}
