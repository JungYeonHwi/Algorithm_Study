function solution(num_list) {
  var answer = 0;

  let wkr = num_list.filter((item) => item % 2 === 0).join("");
  let ghf = num_list.filter((item) => item % 2 !== 0).join("");

  answer = Number(wkr) + Number(ghf);

  return answer;
}
