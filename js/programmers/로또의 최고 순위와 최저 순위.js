function solution(lottos, win_nums) {
  var answer = [];

  let min = lottos.filter((item) => win_nums.includes(item)).length;
  let zero = lottos.filter((item) => item === 0).length;
  let max = min + zero;

  if (min === 0) min = 1;
  if (max === 0) max = 1;

  answer = [Math.abs(7 - max), Math.abs(7 - min)];

  return answer;
}
