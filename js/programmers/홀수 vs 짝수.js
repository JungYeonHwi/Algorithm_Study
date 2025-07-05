function solution(num_list) {
  var answer = 0;

  let wkrtn = num_list.filter((item, index) => index % 2 === 0);
  let ghftn = num_list.filter((item, index) => index % 2 !== 0);

  let wkrtnSum = wkrtn.reduce((a, b) => a + b);
  let ghftnSum = ghftn.reduce((a, b) => a + b);

  answer = Math.max(wkrtnSum, ghftnSum);

  return answer;
}
